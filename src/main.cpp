// src/main.cpp
#include "crow_all.h"

int main() {
    crow::SimpleApp app;

    // Define a route for the root path
    CROW_ROUTE(app, "/")([](){
        return "Hello, World!";
    });

    // Start the server on port 8080
    app.port(8080).multithreaded().run();
}
