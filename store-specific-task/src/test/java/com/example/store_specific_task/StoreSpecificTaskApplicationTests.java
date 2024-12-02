package com.example.store_specific_task;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.annotation.Import;

@Import(TestcontainersConfiguration.class)
@SpringBootTest
class StoreSpecificTaskApplicationTests {

	@Test
	void contextLoads() {
	}

}
