package main

import (
	"io"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	r.GET("/api/crawl", func(c *gin.Context) {
		url := c.Query("url")
		if url == "" {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Missing url parameter"})
			return
		}

		// Assuming crawl4ai service is running on port 8000
		resp, err := http.Get("http://127.0.0.1:8000/crawl?url=" + url)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		defer resp.Body.Close()

		body, err := io.ReadAll(resp.Body)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}

		c.Data(resp.StatusCode, "application/json", body)
	})

	log.Println("Starting server on :8080")
	if err := r.Run(":8080"); err != nil {
		log.Fatalf("Failed to run server: %v", err)
	}
}
