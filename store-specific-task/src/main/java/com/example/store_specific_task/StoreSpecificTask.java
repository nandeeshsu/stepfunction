package com.example.store_specific_task;

import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
@Slf4j
public class StoreSpecificTask implements CommandLineRunner {
    @Override
    public void run(String... args) throws Exception {
        log.info("StoreSpecificTask completed running with starting store {}, and ending store {}",
                System.getenv("Start"), System.getenv("End"));
        log.info("Exited with System.exit(1)");
        System.exit(1);
    }
}
