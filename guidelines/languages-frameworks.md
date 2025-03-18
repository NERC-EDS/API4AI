# Programming Languages, Frameworks and Platforms for APIs  


Technology evolves rapidly, and the programming languages and frameworks used within the EDS organisations (BGS, CEH, NOC) must adapt accordingly. Below is a list of commonly used programming languages and frameworks, along with some potential alternatives.

This document does not mandate the use of any specific technology, as new tools emerge and existing ones evolve. What is considered a best practice today may no longer be the preferred choice in 18 months time. Teams are encouraged to evaluate technologies based on project requirements, long-term maintainability, and industry trends.

By maintaining flexibility in our technology choices, we can ensure that our solutions remain modern, efficient, and well-supported.

## Java
[Java](https://www.java.com/en/) is a robust and versatile programming language widely used for developing APIs, especially in enterprise environments. Its strong typing, object-oriented nature, and extensive libraries make it ideal for building scalable and secure APIs. Java APIs can handle high traffic and complex transactions, making them suitable for large-scale applications.

### Frameworks  

- **Spring Boot (recommended):** Simplifies the development of production-ready applications with its convention-over-configuration approach.
- **Javalin (simple, prototyping):** A lightweight and flexible framework for Java and Kotlin, designed to be simple and blocking, but can switch to asynchronous mode if needed. It supports OpenAPI and runs on top of Jetty, making it easy to configure and use. 
- **Quarkus (alternative):** Optimised for Kubernetes and serverless computing, Quarkus offers ultra-fast boot times and reduced resource consumption1.
- **Micronaut (alternative):**  Micronaut: Known for its fast startup time and low memory consumption, Micronaut is ideal for microservices and serverless applications1.

## JavaScript/TypeScript
[JavaScript](https://en.wikipedia.org/wiki/JavaScript)/[TypeScript](https://www.typescriptlang.org/), particularly with Node.js, is a popular choice for developing APIs due to its non-blocking, event-driven architecture. Node.js allows developers to use JavaScript for both client-side and server-side development, promoting code reuse and faster development cycles. Its asynchronous nature makes it well-suited for handling multiple concurrent connections efficiently.

### Frameworks  
- **Express.js: (recommended)** A minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications.
- **NestJS  (alternative):**  A progressive Node.js framework built with TypeScript, inspired by Angular. It provides an out-of-the-box application architecture for creating scalable and maintainable server-side applications2. Java Equivalent: Spring Boot.
- **Next.js (alternative):**  A React framework that enables server-side rendering and static site generation, making it ideal for building modern web applications3.  

## Python
[Python](https://www.python.org/) is known for its simplicity and readability, making it a great choice for developing APIs. Its extensive standard library and third-party modules allow for rapid development and integration with other services. Python's versatility makes it suitable for various applications, from web development to data science.

### Frameworks 

- **FastAPI (recommended):** A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Django REST Framework: (alternative)** A powerful and flexible toolkit for building Web APIs, built on top of the Django framework.
- **Flask  (alternative):** A micro-framework for Python, perfect for small to medium-sized applications.



## Ruby (alternative)
[Ruby](https://www.ruby-lang.org/en/), with frameworks like Ruby on Rails, is known for its developer-friendly syntax and rapid development capabilities, making it a choice for API development.

### Frameworks 
- **Ruby on Rails:** A full-stack framework that emphasises convention over configuration, making it easy to develop robust APIs quickly Java Equivalent: Spring Boot1.
- **Sinatra:** A lightweight and flexible DSL for building simple and modular web applications and APIs
- **Grape:** A REST-like API micro-framework designed to run on Rack or complement existing web applications built with frameworks like Rails

## Go (Golang) (alternative)

[Go](https://go.dev/) is praised for its performance and efficiency. It's a great choice for building high-performance APIs, especially when dealing with concurrent operations.

### Frameworks 

- **Gin:** A high-performance framework known for its speed and minimalistic design, ideal for building scalable APIs   Java Equivalent: Spring Boot
- **Beego:** A comprehensive framework that offers an all-in-one solution for building web applications and APIs, with built-in features like an HTTP server and ORM
- **Echo:** A minimalist yet feature-rich framework focused on high performance and developer productivity, perfect for RESTful APIs

## C# (alternative) 
 
[C#](https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/) is a strong choice for building APIs, especially in the context of Microsoft environments. ASP\.NET Core is a powerful framework for API development.

### Frameworks 

- **ASP\.NET Core:** A powerful, cross-platform framework for building modern, high-performance web applications and APIs     Java Equivalent: Spring Boot4.
- **Nancy:** A lightweight framework for building HTTP-based services, known for its simplicity and ease of use
- **ServiceStack:** A full-featured framework for building APIs and web services, offering high performance and a wide range of features

### NoCode/LowCode
 
- **[Oracle APEX](https://apex.oracle.com/en/) (Application Express):** is a low-code development platform that allows developers to build scalable and secure web applications, including APIs. It provides a declarative development environment, making it easy to create RESTful web services that interact with Oracle databases.

- ANY OTHERS ???

## Platforms

While this document primarily covers programming languages and frameworks, certain tools and platforms play a key role in our development ecosystem.

### pygeoapi 
[pygeoapi](https://pygeoapi.io/) is an open-source solution for building geospatial APIs that comply with OGC API standards. It provides a ready-to-use implementation for serving spatial data without requiring developers to build an API from scratch.

While pygeoapi is a powerful and lightweight solution for serving OGC APIs, it does have some limitations. One of its primary shortcomings is that it only supports a single flat database table per collection. This design makes it challenging to work with complex or hierarchical data structures, such as multi-table relational models, nested JSON objects, or linked geospatial features.

Workarounds exist, such as denormalising data and pre-processing relationships to flatten the dataset. An additional approach we implemented was embedding **JSON objects** within flattened tables to represent complex structures while maintaining compatibility with pygeoapi’s single-table model.

### ANY OTHERS ???

---

> The landscape of programming languages, frameworks, and tools is vast and  evolving. While we could attempt to list every possible option, new technologies emerge regularly, making it impractical to maintain an exhaustive list. The languages and frameworks outlined above represent the commonly recommended choices at the time of writing, based on their adoption, stability, and suitability for API development. 


