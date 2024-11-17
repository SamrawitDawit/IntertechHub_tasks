package handler

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func Handler(w http.ResponseWriter, r *http.Request) {
	gin.SetMode(gin.ReleaseMode)
	router := gin.Default()

	router.GET("/", func(c *gin.Context) {
		c.Writer.Header().Set("Content-Type", "text/plain")
		c.String(200, "Welcome to my API...to get my name, hobby and dream, please use the following endpoints: /name, /hobby, /dream")
	})

	router.GET("/name", func(c *gin.Context) {
		c.Writer.Header().Set("Content-Type", "text/plain")
		c.String(200, "Samrawit Dawit")
	})
	router.GET("/hobby", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"1)": "Chatting with friends",
			"2)": "Reading",
			"3)": "Watching Movies",
		})
	})
	router.GET("/dream", func(c *gin.Context) {
		c.Writer.Header().Set("Content-Type", "text/plain")
		c.String(200, "To solve people's problem using technology")
	})

	router.ServeHTTP(w, r)
}

func main() {
	http.HandleFunc("/", Handler)
}
