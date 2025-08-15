package main

import (
	"errors"
	"log"
	"net/http"
	"os"

	"github.com/gorilla/websocket"
	"github.com/joho/godotenv"
)

// type OrderBook struct {
// 	ID
// 	Buys
// }

type BinanceRequest struct {
	ID     string                 `json:"id"`
	Method string                 `json:"method"`
	Params map[string]interface{} `json:"params"`
}

type BinanceResponse struct {
	ID     string                 `json:"id"`
	Status int                    `json:"status"`
	Result map[string]interface{} `json:"result,omitempty"`
	Error  map[string]interface{} `json:"error,omitempty"`
}

func LoadAPIKeys() (string, string, error) {
	if err := godotenv.Load("../../.env"); err != nil {
		return "", "", err
	}

	AK := os.Getenv("BINANCE_API_KEY")
	SK := os.Getenv("BINANCE_SECRET_KEY")

	if AK == "" || SK == "" {
		return "", "", errors.New("API keys not found in environment variables")
	}

	return AK, SK, nil
}

func connectWebSocket() (*websocket.Conn, error) {
	testnetURL := "wss://ws-api.testnet.binance.vision/ws-api/v3"
	headers := http.Header{}
	headers.Set("User-Agent", "Adi")
	conn, _, err := websocket.DefaultDialer.Dial(testnetURL, headers)
	if err == nil {
		return conn, nil
	}
	return nil, err
}

/*
Binance sends a ping, we need to send a pong back.
*/
func sendPingFrame(conn *websocket.Conn, req BinanceRequest) (BinanceRequest, error) {

	err := conn.WriteJSON(req)
	if err != nil {
		log.Printf("cannot write req as json")
		return BinanceRequest{}, err
	}
	return req, nil
}

/*
Binance sends a ping, we need to send a pong back.
*/
// func sendPongFrame() (*websocket.Conn, error, BinanceRequest) {
// }

func readResponse(conn *websocket.Conn) (*BinanceResponse, error) {
	var response BinanceResponse
	/*
		The ReadJSON method reads a JSON message from
		WebSocket connection and unmarshals
		it into the struct pointed to by &response.
		It directly modifies the memory at that address,
		populating the fields of the response struct with values
		from the JSON.

	*/
	if err := conn.ReadJSON(&response); err != nil {
		log.Printf("Failed to read response: %v", err)
		return nil, err
	}

	log.Printf("Received response: ID=%s, Status=%d", response.ID, response.Status)

	if response.Status == 200 {
		log.Printf("wss connection successful")
	} else {
		log.Printf("wss connection test failed; status: %d", response.Status)
		if response.Error != nil {
			log.Printf("error details: %+v", response.Error)
		}
	}

	return &response, nil
}
