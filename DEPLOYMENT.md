# 🚀 Cloud Deployment Guide

Deploy your Spam Detection API to the cloud so it's accessible to everyone!

## 🌟 Recommended Deployment Options

### 1. Railway (Recommended - Easiest)
**Best for**: Quick deployment, automatic scaling, free tier available

#### Steps:
1. **Sign up**: Go to [railway.app](https://railway.app) and sign up with GitHub
2. **Connect Repository**: 
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
3. **Deploy**: Railway will automatically detect it's a Python app and deploy
4. **Get URL**: Your API will be available at `https://your-app-name.railway.app`

#### Railway Configuration:
- ✅ `railway.json` - Already created
- ✅ `Procfile` - Already created  
- ✅ Port configuration - Already updated in `app.py`

### 2. Render (Free Alternative)
**Best for**: Free hosting, good for small projects

#### Steps:
1. **Sign up**: Go to [render.com](https://render.com) and sign up with GitHub
2. **Create Web Service**:
   - Connect your GitHub repository
   - Choose "Web Service"
   - Build Command: `pip install -r requirements_fastapi.txt`
   - Start Command: `python app.py`
   - Health Check Path: `/health`
3. **Deploy**: Click "Create Web Service"

#### Render Configuration:
- ✅ `render.yaml` - Already created
- ✅ Health check endpoint - Already configured

### 3. Heroku (Classic Choice)
**Best for**: Established platform, good documentation

#### Steps:
1. **Install Heroku CLI**: Download from [heroku.com](https://heroku.com)
2. **Login**: `heroku login`
3. **Create App**: `heroku create your-spam-detection-api`
4. **Deploy**: `git push heroku main`

#### Heroku Configuration:
- ✅ `Procfile` - Already created
- ✅ Port configuration - Already updated

## 🔧 Pre-Deployment Checklist

### ✅ Files Created:
- `Procfile` - For Heroku/Railway
- `railway.json` - For Railway optimization
- `render.yaml` - For Render configuration
- Updated `app.py` - Dynamic port configuration

### ✅ Backend Features:
- CORS enabled for all origins (`*`)
- Health check endpoint (`/health`)
- Dynamic port configuration
- All ML models pre-trained on startup

## 🌐 After Deployment

### 1. Update Frontend Configuration
Once deployed, update your frontend to use the cloud backend:

```typescript
// In lib/api.ts, change the base URL:
const API_BASE_URL = 'https://your-app-name.railway.app'; // or your deployed URL
```

### 2. Test Your Deployed API
```bash
# Health check
curl https://your-app-name.railway.app/health

# Test spam detection
curl -X POST "https://your-app-name.railway.app/detect" \
  -H "Content-Type: application/json" \
  -d '{"text": "Win money now!", "model": "logistic"}'
```

## 🚀 Quick Start Commands

### Railway (Recommended):
1. Push code to GitHub
2. Connect to Railway
3. Deploy automatically
4. Get your URL!

### Render:
1. Push code to GitHub  
2. Connect to Render
3. Configure build settings
4. Deploy!

### Heroku:
```bash
# Install Heroku CLI first
heroku login
heroku create your-spam-detection-api
git push heroku main
```

## 📊 Performance Considerations

### Model Loading:
- Models are trained on startup (takes ~30 seconds)
- Consider using pre-trained model files for faster startup
- Railway/Render will handle this automatically

### Memory Usage:
- Your app uses ~500MB RAM with all models loaded
- Railway free tier: 512MB (perfect fit!)
- Render free tier: 512MB (perfect fit!)

## 🔒 Security Notes

### CORS Configuration:
- Currently set to `allow_origins=["*"]` for development
- For production, specify your frontend domain:
```python
allow_origins=["https://your-frontend.vercel.app"]
```

### Environment Variables:
- No sensitive data in your current setup
- All models are trained on public datasets
- No API keys required

## 🆘 Troubleshooting

### Common Issues:

1. **Build Fails**: 
   - Check `requirements_fastapi.txt` has all dependencies
   - Ensure Python version compatibility

2. **Models Don't Load**:
   - Check if dataset files are in the repository
   - Verify file paths in `app.py`

3. **CORS Errors**:
   - Update `allow_origins` in `app.py`
   - Check frontend is calling correct URL

### Debug Commands:
```bash
# Check if API is running
curl https://your-app-url/health

# Test spam detection
curl -X POST "https://your-app-url/detect" \
  -H "Content-Type: application/json" \
  -d '{"text": "test message", "model": "logistic"}'
```

## 🎯 Next Steps

1. **Deploy to Railway** (easiest option)
2. **Update frontend** to use cloud backend
3. **Deploy frontend** to Vercel
4. **Share your spam detection app** with the world!

---

**Happy Deploying! 🚀✨**
