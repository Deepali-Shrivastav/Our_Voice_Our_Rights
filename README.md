# Our Voice, Our Rights - MGNREGA Dashboard for Maharashtra

## Project Overview
This Django web application provides accessible MGNREGA (Mahatma Gandhi National Rural Employment Guarantee Act) data for rural citizens of Maharashtra. The interface is designed for low-literacy users with Hindi language support, visual icons, and text-to-speech functionality.

## Features Implemented

### Core Functionality
1. **District-based MGNREGA Data Display**
   - Covers all 36 districts of Maharashtra
   - Shows employment statistics, payment timeliness, and grievances
   - Historical time-series data for trend analysis

2. **User-Friendly Interface**
   - Hindi language interface with visual icons
   - Mobile-responsive design
   - Large, accessible buttons and text
   - Color-coded performance indicators

3. **Geolocation Support**
   - Auto-detect user's district based on GPS location
   - Manual district selection available
   - Nearest district calculation using centroid coordinates

4. **Data Visualization**
   - Key Performance Indicators (KPIs) displayed prominently
   - Month-by-month trend cards
   - Interactive elements for detailed views

5. **Accessibility Features**
   - Text-to-speech support for reading statistics
   - Large font sizes for readability
   - Icon-based navigation
   - High contrast colors

### Technical Implementation

#### Backend (Django 5.0)
- **Models**: District and MGNREGAData models for database storage
- **Views**: API endpoints for cached data and static page serving
- **Caching**: JSON-based local caching system for offline functionality
- **Management Commands**: fetch_mgnrega_data for API integration (extensible)

#### Frontend
- **Single-page application** using vanilla JavaScript
- **No external dependencies** for faster loading
- **Responsive CSS** for mobile-first design
- **Web Speech API** integration for text-to-speech

#### Data Coverage
- **All 36 Maharashtra Districts** with accurate coordinates
- **Realistic MGNREGA metrics** including:
  - Employment provided (monthly)
  - Payment timeliness (percentage)
  - Average payment delays (days)
  - Active projects count
  - Open grievances count
  - 3-month historical data per district

## Project Structure
```
/
├── django_project/          # Main Django project
│   ├── settings.py         # Configuration (ALLOWED_HOSTS, INSTALLED_APPS, etc.)
│   ├── urls.py             # URL routing
│   └── wsgi.py             # WSGI application
├── dashboard/              # Main app
│   ├── models.py           # District and MGNREGAData models
│   ├── views.py            # View functions
│   ├── urls.py             # App-level URL patterns
│   ├── management/         # Custom management commands
│   │   └── commands/
│   │       └── fetch_mgnrega_data.py
│   └── migrations/         # Database migrations
├── static/                 # Static files
│   └── index.html          # Main frontend application
├── cache.json              # Cached MGNREGA data
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## Configuration

### Environment Variables
- Optional: additional domains for CSRF protection (set via environment variable)
- Database: SQLite (default, included)
- Timezone: Asia/Kolkata

### Django Settings
- `DEBUG = True` (development)
- `ALLOWED_HOSTS = ['*']` (allows all hosts)
- `TIME_ZONE = 'Asia/Kolkata'`
- Static files served from `/static/`

## Running the Application

### Development
```bash
python manage.py runserver 0.0.0.0:5000
```

### Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### Fetch Fresh Data (extensible)
```bash
python manage.py fetch_mgnrega_data
```

## Default State
- **Default State**: Maharashtra (hardcoded)
- **Default District**: Pune (shown on page load)
- **Data Source**: Cached JSON file (cache.json)

## Mobile Optimization
- Viewport meta tag for proper scaling
- Touch-friendly button sizes (minimum 44x44 pixels)
- Responsive layout adapts to screen size
- Fast loading with minimal dependencies

## Accessibility Considerations
1. **Language**: Hindi primary, with English technical terms
2. **Icons**: Visual representation for each metric
3. **Color coding**: Green/amber/red for performance indicators
4. **Voice support**: Text-to-speech for key statistics
5. **Large text**: Minimum 16px font size for readability

## Data Caching Strategy
- Primary data stored in `cache.json`
- Fallback mechanism when API unavailable
- Can be extended with database models for persistent storage
- Management command ready for API integration

## Future Enhancements
1. Real-time API integration with data.gov.in
2. Multi-language support (Hindi, English)
3. Chart visualizations (bar/line charts)
4. Comparison between districts
5. Download reports as PDF
6. Push notifications for updates
7. Admin panel for data management

## Dependencies
- Django 5.0+
- Python 3.10+
- requests (for API calls)

## Browser Compatibility
- Modern browsers with JavaScript enabled
- Geolocation API support (optional)
- Web Speech API support (optional)
- Mobile browsers (iOS Safari, Chrome, Firefox)

## License & Credits
Built for the "Our Voice, Our Rights" initiative to make MGNREGA data accessible to rural Maharashtra citizens.


