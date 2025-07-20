# Software de Votación 🗳️

Este es un proyecto de práctica avanzada donde desarrollé un sistema de votación electrónico compuesto por un **frontend en Angular** y múltiples microservicios backend, cada uno implementado con tecnologías diferentes:

- 🔐 Un **API Gateway en Java** para enrutar las solicitudes.
- 👤 Un **microservicio de gestión de usuarios** en Java con Spring Boot.
- 🧮 Un **microservicio de resultados de votación** en Python con Flask y MongoDB.
- 🖥️ Un **frontend en Angular** para interacción con el usuario.

Este proyecto explora una arquitectura distribuida basada en microservicios y demuestra el uso de múltiples lenguajes y frameworks coordinados entre sí.

---

## 🧩 Arquitectura general

[ Angular (Frontend) ]
↓
[ API Gateway - Java ]
↙ ↘
[ Gestión Usuarios - Java ] [ Resultados - Python + Flask + MongoDB ]

yaml
Copy
Edit

---

## ✨ Funcionalidades principales

- Registro y autenticación de votantes.
- Gestión de candidatos y elecciones.
- Emisión de votos por parte del usuario.
- Conteo de votos y consulta de resultados.
- Interacción en tiempo real con la API Gateway.
- Persistencia en base de datos (MongoDB para resultados).

---

## ⚙️ Tecnologías usadas

| Componente        | Stack                         |
|-------------------|-------------------------------|
| Frontend          | Angular, TypeScript, SCSS     |
| API Gateway       | Java, Spring Boot             |
| Gestión usuarios  | Java, Spring Boot, JWT        |
| Resultados        | Python, Flask, MongoDB        |
| Comunicación      | HTTP/REST entre microservicios |

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/dgonzalez-17/software_votacion.git
cd software_votacion
```
2. Ejecutar cada componente
🧠 Backend - API Gateway y Gestión de Usuarios (Java)
```bash
cd api-gateway
# Asegúrate de tener Java y Maven
mvn spring-boot:run
```
```bash
cd ../api-gestionusuarios/ms_usuarios
mvn spring-boot:run
```bash
🧪 Backend - Resultados (Python)
```bash
cd ../api-resultados
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python app.py
```
Asegúrate de tener MongoDB corriendo localmente o en una URI remota.

🖥️ Frontend (Angular)
```bash
cd ../frontend
npm install
ng serve
```
## 📌 Estado del proyecto
Este fue un proyecto de práctica personal (o muestra académica), enfocado en diseñar una solución multilenguaje y multiproceso con componentes desacoplados.
Aunque no está desplegado, representa un buen ejemplo de cómo manejar una arquitectura realista y escalable.
