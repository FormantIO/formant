package main

import (
	"bytes"
	"context"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"time"

	"github.com/FigureWorks/figure/examples/go/agent"

	"google.golang.org/grpc"
)

func streamData() {
	go func() {
		for {

			conn, err := grpc.Dial("localhost:5501", grpc.WithInsecure())
			if err != nil {
				log.Printf("Could not connect to agent/server")
			}
			defer conn.Close()
			agentClient := agent.NewAgentClient(conn)
			stream, err := agentClient.StreamData(context.Background())
			if err != nil {
				log.Printf("Could not create Data Stream %v", err)
				//Retry
				time.Sleep(time.Second)
				streamData()
			}
			timestampMs := time.Now().UnixNano() / int64(time.Millisecond)
			datapoint := "i am a streaming datapoint"
			data := &agent.Datapoint{
				Stream:    "stream.001",
				Timestamp: timestampMs,
				Data: &agent.Datapoint_Text{
					Text: &agent.Text{
						Value: datapoint,
					},
				},
			}
			err = stream.Send(data)
			if err != nil {
				log.Printf("Error streaming data %v", err)
			}
			time.Sleep(time.Millisecond * 200)
		}
	}()

}

func postData() {
	conn, err := grpc.Dial("localhost:5501", grpc.WithInsecure())
	if err != nil {
		log.Printf("Could not connect to agent/server")
	}
	defer conn.Close()
	agentClient := agent.NewAgentClient(conn)
	timestampMs := time.Now().UnixNano() / int64(time.Millisecond)
	datapoint := "i am a posted datapoint"
	data := &agent.Datapoint{
		Stream:    "stream.001",
		Timestamp: timestampMs,
		Data: &agent.Datapoint_Text{
			Text: &agent.Text{
				Value: datapoint,
			},
		},
	}
	_, err = agentClient.PostData(context.Background(), data)
	if err != nil {
		log.Printf("Error posting data %v", err)
	}
}
func postNumericData() {
	conn, err := grpc.Dial("localhost:5501", grpc.WithInsecure())
	if err != nil {
		log.Printf("Could not connect to agent/server")
	}
	defer conn.Close()
	agentClient := agent.NewAgentClient(conn)
	timestampMs := time.Now().UnixNano() / int64(time.Millisecond)
	datapoint := 2.33
	data := &agent.Datapoint{
		Stream:    "stream.002",
		Timestamp: timestampMs,
		Data: &agent.Datapoint_Numeric{
			Numeric: &agent.Numeric{
				Value: datapoint,
			},
		},
	}
	_, err = agentClient.PostData(context.Background(), data)
	if err != nil {
		log.Printf("Error posting data %v", err)
	}
}

func postHTTPData() {

	datapoint := "this is a http posted datapoint"
	curTime := time.Now().UnixNano() / int64(time.Millisecond)

	var jsonStr = []byte(fmt.Sprintf(`
	{
		"stream": "stream.001",
		"timestamp": %v,
		"text" : { "value" : "%v" }
	}
	`, curTime, datapoint))
	req, err := http.NewRequest("POST", fmt.Sprintf("%v/%v", "http://localhost:5502", "v1/data"), bytes.NewBuffer(jsonStr))
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	fmt.Println("response Status:", resp.Status)
	fmt.Println("response Headers:", resp.Header)
	body, _ := ioutil.ReadAll(resp.Body)
	fmt.Println("response Body:", string(body))
}

func postHTTPNumericData() {
	curTime := time.Now().UnixNano() / int64(time.Millisecond)
	datapoint := 2.33
	var jsonStr = []byte(fmt.Sprintf(`
	{
		"stream": "stream.002",
		"timestamp": %v,
		"numeric" : { "value" : %v }
	}
	`, curTime, datapoint))
	req, err := http.NewRequest("POST", fmt.Sprintf("%v/%v", "http://localhost:5502", "v1/data"), bytes.NewBuffer(jsonStr))
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	fmt.Println("response Status:", resp.Status)
	fmt.Println("response Headers:", resp.Header)
	body, _ := ioutil.ReadAll(resp.Body)
	fmt.Println("response Body:", string(body))
}

func main() {
	postData()
	time.Sleep(time.Millisecond * 200)
	postNumericData()
	time.Sleep(time.Millisecond * 200)
	postHTTPData()
	time.Sleep(time.Millisecond * 200)
	postHTTPNumericData()
	time.Sleep(time.Millisecond * 200)
	streamData()
	for {
	}
}
