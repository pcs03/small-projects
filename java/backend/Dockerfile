# Build
FROM maven:3.9.9 AS build
WORKDIR /app

COPY pom.xml .
COPY src ./src

ENV FLASK_API_HOST="http://localhost:5000"

RUN mvn clean package -DskipTests

# App
FROM openjdk:17-jdk-slim
WORKDIR /app

# RUN groupadd -S spring && useradd -S spring -G spring
# RUN chown spring:spring /app
# USER spring:spring

COPY --from=build /app/target/*.jar app.jar

EXPOSE 8080

ENV FLASK_API_HOST="http://localhost:5000"

ENTRYPOINT ["java", "-jar", "app.jar"]
