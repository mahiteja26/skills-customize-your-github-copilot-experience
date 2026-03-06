# 💰 Assignment: Crypto Portfolio Tracker

## 🎯 Objective

Build a full-stack financial application that integrates with live cryptocurrency APIs and persists user portfolio data to a database. You will consume real market data from the CoinGecko API, store portfolio holdings with FastAPI, calculate gains/losses, and track portfolio history over time.

## 📝 Tasks

### 🛠️ Set Up FastAPI with SQLite Database

#### Description
Create the foundation of your crypto tracker by setting up a FastAPI application with SQLite database integration for storing portfolio data.

#### Requirements
Completed program should:

- Import and initialize FastAPI and SQLAlchemy ORM
- Create a SQLite database connection
- Define database models for:
  - User portfolio holdings (crypto symbol, quantity, purchase price, purchase date)
  - Portfolio snapshots (total value, timestamp for historical tracking)
- Create database tables on startup
- Implement database session management
- Example models:
  ```python
  class Holding(Base):
      id: int
      symbol: str
      quantity: float
      purchase_price: float
      purchase_date: datetime
  ```

### 🛠️ Integrate CoinGecko API for Live Prices

#### Description
Fetch real-time cryptocurrency prices from the CoinGecko API to enable live portfolio valuation.

#### Requirements
Completed program should:

- Use the free CoinGecko API (https://api.coingecko.com/api/v3) to fetch live crypto prices
- Handle API rate limiting and errors gracefully
- Support multiple cryptocurrencies (BTC, ETH, etc.)
- Cache prices to reduce API calls (optional but recommended)
- Return current price data in JSON format
- Example API call:
  ```
  GET /prices?symbols=bitcoin,ethereum
  Response: {"bitcoin": 43500, "ethereum": 2300}
  ```

### 🛠️ Implement Portfolio Management Endpoints

#### Description
Create endpoints to add, view, and manage cryptocurrency holdings in the portfolio.

#### Requirements
Completed program should:

- `POST /holdings` - Add a new cryptocurrency holding to portfolio
- `GET /holdings` - List all current holdings
- `GET /holdings/{symbol}` - Get details for a specific crypto holding
- `PUT /holdings/{symbol}` - Update holdings (e.g., average down or increase position)
- `DELETE /holdings/{symbol}` - Remove a holding from portfolio
- Store all data in SQLite database
- Example POST request:
  ```json
  {
    "symbol": "bitcoin",
    "quantity": 0.5,
    "purchase_price": 43000,
    "purchase_date": "2026-01-15"
  }
  ```

### 🛠️ Calculate and Display Portfolio Metrics

#### Description
Create endpoints that calculate real-time portfolio performance metrics using live API prices and stored holding data.

#### Requirements
Completed program should:

- `GET /portfolio/summary` - Return:
  - Total portfolio value (current)
  - Total invested amount
  - Overall gain/loss (dollar amount and percentage)
  - Best and worst performing holdings
  - Allocation breakdown (percentage per crypto)
- `GET /portfolio/history` - Return portfolio value snapshots over time
- Fetch current prices and calculate metrics dynamically
- Handle edge cases (empty portfolio, single holding)
- Example response:
  ```json
  {
    "total_value": 85000,
    "total_invested": 75000,
    "gain_loss_usd": 10000,
    "gain_loss_percent": 13.33,
    "best_performer": "ethereum",
    "allocations": {"bitcoin": 60, "ethereum": 40}
  }
  ```

### 🛠️ Add Database Persistence for Portfolio History

#### Description
Implement automatic tracking of portfolio snapshots and retrieve historical performance data.

#### Requirements
Completed program should:

- Store portfolio snapshots with timestamp and total value periodically
- Implement `GET /portfolio/history?days=30` to retrieve historical data
- Calculate portfolio performance over different time periods
- Support querying performance for specific date ranges
- Persist all data durably to SQLite database
- Example response:
  ```json
  {
    "timestamps": ["2026-02-01", "2026-02-02", "2026-02-03"],
    "portfolio_values": [70000, 75000, 82000]
  }
  ```

## 📚 Learning Outcomes

By completing this assignment, students will:
- Integrate third-party APIs into a Python application
- Design and work with relational databases using SQLAlchemy ORM
- Build practical financial calculations and metrics
- Handle real-world data challenges (API rate limits, data validation)
- Create a complete full-stack application combining backend APIs and persistent storage
