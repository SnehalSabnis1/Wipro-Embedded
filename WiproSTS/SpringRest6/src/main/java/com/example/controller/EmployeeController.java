package com.example.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.data.Employee;
import com.example.repository.EmployeeRepository;

@RestController
public class EmployeeController {
	
	//http://localhost:8090/Hello
	@GetMapping ("/Hello")
	public String sayHello () {
		return "Hello, Welcome to Spring Boot Application...";
	}
	
	//http://localhost:8090/HelloByName
	@GetMapping ("/HelloByName")
	public String helloByName (@RequestParam String name) {
		String strReturn = "Hello, Welcome to" + name +" from Spring Boot Application...";
		return strReturn;
	}
	
	@PostMapping ("/InsertData")
	public String insertData (@RequestBody Employee empObj) {
		System.out.println("Received data is : "+empObj);
		empRepo.save(empObj);
		return "Record inserted successfully...";
	}
	
	@PutMapping ("/updateData")
	public String updateData (@RequestBody Employee empObj) {
		System.out.println("Received data is : "+empObj);
		empRepo.save(empObj);
		return "Given record is updated in db successfully...";
	}
	
	@DeleteMapping ("/deleteRecord/{id}")
	public String deleteRecord (@PathVariable int id) {
		System.out.println("Given record to delete with employee id is : "+id);
		empRepo.deleteById(id);
		String strReturn = "Record with id" + id +" is deleted in the database successfully...";
		return strReturn;
	}
@Autowired
EmployeeRepository empRepo;
@GetMapping("/getAllData")
public List <Employee> getAllData()
{
	List<Employee> empList=empRepo.findAll();
	return empList;

}

}
