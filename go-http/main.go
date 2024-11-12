package main

import "net/http"

type HomeHandler struct{}

func (h *HomeHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("Hello, World!\n"))
}

func main() {
    mux := http.NewServeMux()
    mux.Handle("/", &HomeHandler{})

    http.ListenAndServe(":8000", mux)
}
