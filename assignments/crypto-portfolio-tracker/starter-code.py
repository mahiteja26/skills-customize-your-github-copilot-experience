"""
Crypto Portfolio Tracker - Capstone Project Starter Code
Build a full-stack crypto portfolio application with live API integration and database persistence.

Install dependencies:
pip install fastapi uvicorn sqlalchemy sqlite3 requests
"""

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
import requests

# Initialize FastAPI app
app = FastAPI(title="Crypto Portfolio Tracker")

# Database setup
DATABASE_URL = "sqlite:///./crypto_portfolio.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# CoinGecko API base URL
COINGECKO_API = "https://api.coingecko.com/api/v3"

# ============================================================================
# DATABASE MODELS
# ============================================================================

class Holding(Base):
    """Database model for storing cryptocurrency holdings"""
    __tablename__ = "holdings"
    
    id = Column(Integer, primary_key=True, index=True)
    # TODO: Add columns for symbol, quantity, purchase_price, purchase_date
    # Example:
    # symbol = Column(String, unique=True, index=True)


class PortfolioSnapshot(Base):
    """Database model for storing historical portfolio values"""
    __tablename__ = "portfolio_snapshots"
    
    id = Column(Integer, primary_key=True, index=True)
    # TODO: Add columns for timestamp and total_value


# Create all database tables
Base.metadata.create_all(bind=engine)


# ============================================================================
# PYDANTIC MODELS (for request/response validation)
# ============================================================================

class HoldingCreate(BaseModel):
    """Schema for creating a new holding"""
    symbol: str
    quantity: float
    purchase_price: float
    purchase_date: str  # "YYYY-MM-DD" format


class HoldingResponse(HoldingCreate):
    """Schema for holding responses"""
    id: int
    
    class Config:
        from_attributes = True


class PortfolioSummary(BaseModel):
    """Schema for portfolio summary response"""
    total_value: float
    total_invested: float
    gain_loss_usd: float
    gain_loss_percent: float
    best_performer: Optional[str]
    allocations: dict


# ============================================================================
# API ENDPOINTS
# ============================================================================

def get_db():
    """Dependency for database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Welcome to Crypto Portfolio Tracker"}


# ============================================================================
# TODO: Implement the following endpoints
# ============================================================================

# 1. GET /prices?symbols=bitcoin,ethereum
#    Fetch current prices from CoinGecko API

# 2. POST /holdings
#    Add a new cryptocurrency holding to portfolio

# 3. GET /holdings
#    List all current holdings

# 4. GET /holdings/{symbol}
#    Get details for a specific holding

# 5. PUT /holdings/{symbol}
#    Update a holding

# 6. DELETE /holdings/{symbol}
#    Remove a holding

# 7. GET /portfolio/summary
#    Return portfolio metrics (total value, gains/losses, allocation)

# 8. GET /portfolio/history?days=30
#    Return historical portfolio values


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def fetch_crypto_price(symbol: str) -> Optional[float]:
    """
    Fetch current price for a cryptocurrency from CoinGecko API
    
    Args:
        symbol (str): Cryptocurrency symbol (e.g., 'bitcoin', 'ethereum')
    
    Returns:
        float: Current price in USD, or None if fetch fails
    """
    # TODO: Implement API call to CoinGecko
    pass


def calculate_portfolio_value(db: Session) -> float:
    """
    Calculate total current portfolio value
    
    Args:
        db (Session): Database session
    
    Returns:
        float: Total portfolio value in USD
    """
    # TODO: Get all holdings, fetch current prices, calculate total value
    pass


def calculate_gains_losses(db: Session) -> tuple:
    """
    Calculate portfolio gains/losses
    
    Args:
        db (Session): Database session
    
    Returns:
        tuple: (total_gain_loss_usd, total_gain_loss_percent)
    """
    # TODO: Compare current portfolio value to total invested amount
    pass


# ============================================================================
# TO RUN THIS APPLICATION:
# ============================================================================
# uvicorn starter-code:app --reload
# Visit: http://localhost:8000 (main app)
# Visit: http://localhost:8000/docs (interactive API documentation)
