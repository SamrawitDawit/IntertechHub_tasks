package router

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func Router() {
	gin.SetMode(gin.ReleaseMode)
	router := gin.Default()
	router.GET("/name", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"Name": "Samrawit Dawit",
		})
	})
	router.GET("/hobby", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"1)": "Chatting with friends",
			"2)": "Reading",
			"3)": "Watching Movies",
		})
	})
	router.GET("/dream", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"Dream": "To solve people's problem using technology",
		})
	})
	http.Handle("/", router)
}
