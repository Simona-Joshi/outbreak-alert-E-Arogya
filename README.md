# E-Aarogya - Nepal Health Ministry Health App

A comprehensive health app section for the Nepal Health Ministry focusing on outbreak alerts, disease tracking, and safety tips with modern UI/UX design.

## 🚀 Features

### 🏠 Home Screen (Outbreak Alerts)
- **Nepal Health Ministry Branding** with official colors
- **Quick Action Cards** for Live Tracker, Outbreaks, Safety Tips, and Emergency
- **Current Alerts List** with color-coded risk levels
- **Emergency Support Card** with hotline information
- **Pull-to-refresh** functionality with smooth animations

### 📊 Live Disease Tracker
- **Real-time GPS Location Detection** for personalized outbreak data
- **Interactive Map** with outbreak markers and risk visualization
- **National Statistics Dashboard** with active outbreaks and case counts
- **Location-based Outbreak Alerts** within 50km radius
- **District Selection** for manual location-based tracking

### 🦠 Outbreak Details
- **Featured Outbreak Alert Card** with risk level indicators
- **Comprehensive Outbreak List** with detailed statistics
- **Color-coded Risk Levels**: High (Red), Medium (Yellow), Low (Green)
- **Quick Action Buttons** for Safety Tips, Live Tracker, and Emergency
- **Real-time Case Statistics** including new cases and recovery rates

### 🛡️ Safety Tips
- **Category-based Filtering**: Prevention, Symptoms, Treatment, Emergency
- **Essential Health Tips Grid** with quick visual guides
- **Disease-specific Safety Guidelines** from backend API
- **Emergency Contact Information** with call and SMS options
- **Interactive Tip Cards** with color-coded categories

## 🎨 Design System

### Color Palette
- **Primary Blue**: `#1E40AF` - Trust and reliability
- **Success Green**: `#059669` - Recovery and health
- **Warning Yellow**: `#F59E0B` - Caution and alerts
- **Danger Red**: `#DC2626` - Critical alerts and emergencies
- **Neutral Gray**: `#6B7280` - Supporting text and backgrounds

### UI/UX Features
- **Rounded Corners** (16px) for modern card design
- **Subtle Shadows** for depth and hierarchy
- **Smooth Animations** with fade-in effects
- **Accessible Color Contrast** for color-blind users
- **Touch-friendly Targets** (minimum 44px)
- **Consistent Typography** with clear hierarchy

## 🛠️ Technology Stack

### Frontend (React Native + Expo)
- **Expo SDK 53** for cross-platform development
- **React Navigation** for tab and screen navigation
- **Expo Location** for GPS and location services
- **React Native Maps** for interactive map visualization
- **Expo Vector Icons** for consistent iconography
- **TypeScript** for type safety and better development experience

### Backend (Django + PostgreSQL)
- **Django 5.0** with REST Framework
- **PostgreSQL** database for robust data storage
- **CORS Headers** for cross-origin requests
- **Custom Management Commands** for data seeding
- **Admin Interface** for content management

## 📱 Installation & Setup

### Prerequisites
- Node.js (v18 or higher)
- Python 3.9+
- PostgreSQL 13+
- Expo CLI (`npm install -g @expo/cli`)

### Frontend Setup
```bash
# Clone the repository
git clone <repository-url>
cd E-Aarogya

# Install dependencies
npm install

# Install additional type definitions
npm install --save-dev @types/react-native-maps

# Start the development server
npx expo start
```

### Backend Setup
DB_NAME=nepal_health_db
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_secret_key
DEBUG=True
```

## 🌐 API Endpoints

### Base URL: `http://localhost:8000/api/v1/`

- **GET** `/districts/` - List all districts
- **GET** `/outbreaks/` - List all outbreak cases
- **GET** `/alerts/` - List all outbreak alerts
- **GET** `/safety-tips/` - List all safety tips
- **GET** `/location-outbreaks/?lat={lat}&lng={lng}` - Location-based outbreaks
- **GET** `/district-outbreaks/{district_id}/` - District-specific outbreaks
- **GET** `/national-overview/` - National statistics overview

## 📂 Project Structure

```
E-Aarogya/
├── app/                          # React Native app
│   ├── (tabs)/                   # Tab-based screens
│   │   ├── index.tsx            # Home screen (Outbreak Alerts)
│   │   ├── livetracker.tsx      # Live Disease Tracker
│   │   ├── outbreakdetails.tsx  # Outbreak Details
│   │   ├── safetytips.tsx       # Safety Tips
│   │   └── _layout.tsx          # Tab navigation layout
│   └── _layout.tsx              # Root layout
├── backend/                      # Django backend
│   ├── health_ministry/         # Main Django project
│   ├── outbreaks/              # Outbreaks app
│   │   ├── models.py           # Database models
│   │   ├── serializers.py      # API serializers
│   │   ├── views.py            # API views
│   │   ├── urls.py             # URL routing
│   │   └── management/         # Custom commands
│   └── requirements.txt        # Python dependencies
├── package.json                # Node.js dependencies
└── README.md                   # This file
```

## 🚀 Deployment

### Frontend (Expo)
```bash
# Build for production
npx expo build:android  # For Android
npx expo build:ios      # For iOS

# Or use EAS Build
npx eas build --platform all
```

### Backend (Django)
```bash
# Collect static files
python manage.py collectstatic

# Set DEBUG=False in production
# Configure production database
# Deploy to your preferred hosting service
```

## 🧪 Testing

### Run Frontend Tests
```bash
npm test
```

### Run Backend Tests
```bash
cd backend
python manage.py test
```

## 📋 Features Checklist

- ✅ **Home Screen** with Nepal Health Ministry branding
- ✅ **Live Disease Tracker** with GPS and map integration
- ✅ **Outbreak Details** with comprehensive statistics
- ✅ **Safety Tips** with category filtering
- ✅ **Django Backend** with PostgreSQL database
- ✅ **REST API** endpoints for all data
- ✅ **Real-time Data** fetching and refresh
- ✅ **Responsive Design** with accessibility features
- ✅ **Color-coded Risk Levels** for easy identification
- ✅ **Emergency Contact** integration
- ✅ **Smooth Animations** and modern UI

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- **Emergency Hotline**: 103
- **Health SMS**: 1115
- **Email**: support@mohp.gov.np
- **Website**: https://mohp.gov.np

## 🙏 Acknowledgments

- Nepal Ministry of Health and Population
- Expo and React Native communities
- Django and PostgreSQL communities
- All contributors and testers

---

**Built with ❤️ for the health and safety of Nepal**
