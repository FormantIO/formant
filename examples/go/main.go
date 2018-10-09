package main

import (
	"bytes"
	"encoding/base64"
	"encoding/binary"
	"fmt"
	"io/ioutil"
	"math"
	"net/http"

	"context"
	"log"
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
			datapoint := []byte("i am a streaming datapoint")
			data := agent.Datapoint{
				Stream:    "stream.001",
				Timestamp: timestampMs,
				Type:      agent.ContentType_TEXT,
				Data:      datapoint,
			}
			err = stream.Send(&data)
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
	datapoint := []byte("i am a posted datapoint")
	data := &agent.Datapoint{
		Stream:    "stream.001",
		Timestamp: timestampMs,
		Type:      agent.ContentType_TEXT,
		Data:      datapoint,
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
	datapointNumeric := make([]byte, 8)
	binary.LittleEndian.PutUint64(datapointNumeric[:], math.Float64bits(2.33))
	dataNumeric := &agent.Datapoint{
		Stream:    "stream.002",
		Timestamp: timestampMs,
		Type:      agent.ContentType_NUMERIC,
		Data:      datapointNumeric,
	}
	_, err = agentClient.PostData(context.Background(), dataNumeric)
	if err != nil {
		log.Printf("Error posting data %v", err)
	}
}

func postHTTPData() {

	datapoint := "this is a http posted datapoint"
	curTime := time.Now().UnixNano() / int64(time.Millisecond)
	encodedDatapoint := base64.StdEncoding.EncodeToString([]byte(datapoint))

	var jsonStr = []byte(fmt.Sprintf(`
	{
		"stream": "stream.001",
		"type": "TEXT",
		"timestamp": %v,
		"data": "%v"
	}
	`, curTime, encodedDatapoint))
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
	datapointNumeric := make([]byte, 8)
	binary.LittleEndian.PutUint64(datapointNumeric[:], math.Float64bits(2.33))
	encodedDatapoint := base64.StdEncoding.EncodeToString(datapointNumeric)

	var jsonStr = []byte(fmt.Sprintf(`
	{
		"stream": "stream.002",
		"type": "NUMERIC",
		"timestamp": %v,
		"data": "%v"
	}
	`, curTime, encodedDatapoint))
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
