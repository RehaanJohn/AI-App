# AI Challenge Generator 🧠

A full-stack web application that generates AI-powered multiple-choice challenges using OpenAI's API. Users can create, take, and review challenges with seamless authentication powered by Clerk.

## ✨ Features

- 🤖 **AI-Powered Question Generation** - Uses OpenAI API to create engaging multiple-choice questions
- 🔐 **Secure Authentication** - Integrated with Clerk for user management and authentication
- 📚 **Challenge History** - Track and review previously generated challenges
- 🎯 **Interactive MCQ Interface** - Clean, responsive multiple-choice question interface
- 🌐 **RESTful API** - Well-structured FastAPI backend with proper error handling
- ⚡ **Modern Frontend** - Built with React and Vite for fast development and deployment

## 🏗️ Architecture

### Backend (`backend/`)
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - Database ORM for data persistence
- **OpenAI Python SDK** - AI question generation
- **Clerk** - User authentication and webhook handling

### Frontend (`frontend/`)
- **React** - Component-based UI library
- **Vite** - Fast build tool and development server
- **Clerk React** - Authentication components
- **Modern CSS** - Responsive design

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- OpenAI API key
- Clerk account and API keys

### Environment Setup

Create `.env` files in both backend and frontend directories:

**Backend `.env`:**
```env
OPENAI_API_KEY=your_openai_api_key_here
CLERK_SECRET_KEY=your_clerk_secret_key_here
DATABASE_URL=sqlite:///app.db
```

**Frontend `.env`:**
```env
VITE_CLERK_PUBLISHABLE_KEY=your_clerk_publishable_key_here
VITE_BACKEND_URL=http://localhost:8000
```

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
python server.py
```

The backend will start on `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will start on `http://localhost:5173`

## 📁 Project Structure

```
AI-APP/
├── backend/
│   ├── src/
│   │   ├── routes/
│   │   │   ├── challenge.py      # Challenge generation endpoints
│   │   │   └── webhooks.py       # Clerk webhook handlers
│   │   ├── database/
│   │   │   ├── db.py            # Database configuration
│   │   │   └── models.py        # SQLAlchemy models
│   │   ├── ai_generator.py      # OpenAI integration
│   │   ├── app.py              # FastAPI application
│   │   └── utils.py            # Helper functions
│   ├── server.py               # Application entrypoint
│   ├── .env                    # Backend environment variables
│   └── requirements.txt        # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── auth/
│   │   │   ├── AuthenticationPage.jsx
│   │   │   └── ClerkProviderWithRoutes.jsx
│   │   ├── challenge/
│   │   │   ├── ChallengeGenerator.jsx
│   │   │   └── MCQChallenge.jsx
│   │   ├── history/
│   │   │   └── HistoryPanel.jsx
│   │   ├── layout/
│   │   │   └── Layout.jsx
│   │   ├── utils/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── .env                    # Frontend environment variables
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

## 🔧 API Endpoints

### Challenge Routes
- `POST /api/challenge/generate` - Generate a new AI challenge
- `GET /api/challenges` - Retrieve user's challenge history
- `GET /api/challenge/{id}` - Get specific challenge details

### Webhook Routes
- `POST /api/webhooks/clerk` - Handle Clerk user events

## 🎯 Usage

1. **Sign Up/Login**: Create an account or sign in using Clerk authentication
2. **Generate Challenge**: Use the challenge generator to create AI-powered questions
3. **Take Challenge**: Answer the multiple-choice questions
4. **View History**: Review your previous challenges and performance

## 🛠️ Development

### Running Tests
```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

### Code Formatting
```bash
# Backend (using black)
cd backend
black .

# Frontend (using prettier)
cd frontend
npm run format
```

## 📝 Environment Variables Reference

### Backend Environment Variables
- `OPENAI_API_KEY` - Your OpenAI API key for generating questions
- `CLERK_SECRET_KEY` - Clerk secret key for backend authentication
- `DATABASE_URL` - Database connection string (SQLite by default)

### Frontend Environment Variables
- `VITE_CLERK_PUBLISHABLE_KEY` - Clerk publishable key for frontend
- `VITE_BACKEND_URL` - Backend API URL

## 🚀 Deployment

### Backend Deployment
The backend can be deployed to platforms like:
- **Heroku** - Add `Procfile`: `web: python server.py`
- **Railway** - Automatic deployment from Git
- **Docker** - Create `Dockerfile` with Python runtime

### Frontend Deployment
The frontend can be deployed to:
- **Vercel** - Automatic deployment with Git integration
- **Netlify** - Static site deployment
- **GitHub Pages** - Free static hosting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Clerk Documentation](https://clerk.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the [Issues](../../issues) section
2. Create a new issue with detailed information
3. Contact the development team

---

Made with ❤️ by [Your Name/Team]
