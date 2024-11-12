package nl.conclusion.backend.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@RestController
@RequestMapping("/api/v1")
public class ApiController {

    private String apiUri;
    private final RestTemplate restTemplate = new RestTemplate();
    private Logger logger;

    @Autowired
    public ApiController() {
        this.logger = LoggerFactory.getLogger(ApiController.class);
        String apiHost = System.getenv("FLASK_API_HOST");
        this.apiUri = apiHost + "/api/v1";
        logger.info("FLASK API HOST:" + this.apiUri);
    }

    @GetMapping("/select")
    public ResponseEntity<String> selectData() {
        String url = this.apiUri + "/select";
        this.logger.info("Request to: " + url);
        ResponseEntity<String> response = restTemplate.getForEntity(url, String.class);
        return ResponseEntity.ok(response.getBody());
    }

    @PostMapping("/insert")
    public ResponseEntity<String> insertData(@RequestBody Map<String, String> requestBody) {
        String url = this.apiUri + "/insert";
        this.logger.info("Request to: " + url);
        ResponseEntity<String> response = restTemplate.postForEntity(url, requestBody, String.class);
        return ResponseEntity.ok(response.getBody());
    }
}
