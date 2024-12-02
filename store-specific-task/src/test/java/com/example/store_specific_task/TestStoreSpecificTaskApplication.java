package com.example.store_specific_task;

import org.springframework.boot.SpringApplication;

public class TestStoreSpecificTaskApplication {

	public static void main(String[] args) {
		SpringApplication.from(StoreSpecificTaskApplication::main).with(TestcontainersConfiguration.class).run(args);
	}

}
