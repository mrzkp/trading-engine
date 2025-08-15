package main

import (
	"log"
	"time"

	"github.com/gorilla/websocket"
)

func main() {
	// Load API keys
	var AK, SK string
	var err error

	AK, SK, err = LoadAPIKeys()
	if err != nil {
		log.Fatalf("Failed to load API keys: %v", err)
	}

	log.Printf(AK)
	log.Printf(SK)
	log.Printf("API keys loaded successfully")

	// Establish wss connection
	var conn *websocket.Conn
	for {
		conn, err = connectWebSocket()
		if err == nil {
			log.Println("Connected to Binance WebSocket API")
			break
		}
		log.Printf("Connection failed: %v. Retrying in 5 seconds...", err)
		time.Sleep(5 * time.Second)
	}
	defer conn.Close() // schedules func call when main exists;

	// Send ping test connection
	req := BinanceRequest{
		ID:     "egia9gjeoa123123",
		Method: "ping",
		Params: make(map[string]interface{}),
	}
	sendPingFrame(conn, req)
	log.Println("Sent ping request")

	// Read response
	_, err = readResponse(conn)
	if err != nil {
		log.Printf("Failed to process response: %v", err)
		return
	}
}
