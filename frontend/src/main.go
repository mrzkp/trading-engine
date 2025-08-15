package src

import (
	"log"
	"time"

	"github.com/gorilla/websocket"
)

type OrderBook struct {
	Buys  map[string]float64
	Sells map[string]float64
}

func InitOrderBook() *OrderBook {
	return &OrderBook{
		Buys:  make(map[string]float64),
		Sells: make(map[string]float64),
	}
}

func main() {
	symbol := "btcusdt"
	base_url := "wss://stream.binance.com:9443/stream?streams=" + symbol

	var conn *websocket.Conn
	var err error
	// new_order_book := InitOrderBook()

	for {
		conn, _, err = websocket.DefaultDialer.Dial(base_url, nil)
		if err != nil {
			log.Printf("cnnect error")
			time.Sleep(5 * time.Second)
			continue
		}
		log.Println("connected")
	}

}
