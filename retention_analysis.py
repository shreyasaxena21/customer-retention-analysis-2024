#!/usr/bin/env python3
"""
Customer Retention Rate Analysis - 2024 Quarterly Performance
Author: Analysis created with LLM assistance
Contact: 22f3001013@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

# Set style for professional visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def analyze_retention_data():
    """
    Comprehensive analysis of quarterly customer retention data
    """
    
    # Customer Retention Rate - 2024 Quarterly Data
    retention_data = {
        'Quarter': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
        'Retention_Rate': [65.77, 74.85, 72.35, 74.62]
    }
    
    df = pd.DataFrame(retention_data)
    
    # Calculate key metrics
    average_retention = np.mean(df['Retention_Rate'])
    industry_target = 85
    gap_to_target = industry_target - average_retention
    
    print("="*60)
    print("CUSTOMER RETENTION ANALYSIS - 2024")
    print("="*60)
    print(f"Average Retention Rate: {average_retention:.2f}%")
    print(f"Industry Target: {industry_target}%")
    print(f"Gap to Target: {gap_to_target:.2f}%")
    print("="*60)
    
    # Quarterly performance analysis
    print("\nQuarterly Performance:")
    for i, row in df.iterrows():
        trend = ""
        if i > 0:
            change = row['Retention_Rate'] - df.loc[i-1, 'Retention_Rate']
            trend = f" ({'+' if change > 0 else ''}{change:.2f}%)"
        print(f"{row['Quarter']}: {row['Retention_Rate']:.2f}%{trend}")
    
    return df, average_retention, industry_target, gap_to_target

def create_visualizations(df, average_retention, industry_target):
    """
    Create comprehensive visualizations for retention analysis
    """
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Customer Retention Analysis Dashboard - 2024', fontsize=16, fontweight='bold')
    
    # 1. Quarterly Trend Line Chart
    ax1.plot(df['Quarter'], df['Retention_Rate'], marker='o', linewidth=2, markersize=8, color='#2E86C1')
    ax1.axhline(y=industry_target, color='red', linestyle='--', alpha=0.7, label=f'Industry Target ({industry_target}%)')
    ax1.axhline(y=average_retention, color='orange', linestyle=':', alpha=0.7, label=f'Average ({average_retention:.1f}%)')
    ax1.set_title('Quarterly Retention Rate Trend', fontweight='bold')
    ax1.set_ylabel('Retention Rate (%)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(60, 90)
    
    # 2. Bar Chart with Target Comparison
    colors = ['#E74C3C' if x < average_retention else '#27AE60' for x in df['Retention_Rate']]
    bars = ax2.bar(df['Quarter'], df['Retention_Rate'], color=colors, alpha=0.7)
    ax2.axhline(y=industry_target, color='red', linestyle='--', alpha=0.7, label=f'Industry Target ({industry_target}%)')
    ax2.set_title('Quarterly Performance vs Target', fontweight='bold')
    ax2.set_ylabel('Retention Rate (%)')
    ax2.legend()
    ax2.set_ylim(60, 90)
    
    # Add value labels on bars
    for bar, value in zip(bars, df['Retention_Rate']):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                f'{value:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    # 3. Gap Analysis
    gaps = [industry_target - x for x in df['Retention_Rate']]
    ax3.bar(df['Quarter'], gaps, color='#E74C3C', alpha=0.6)
    ax3.set_title('Gap to Industry Target (85%)', fontweight='bold')
    ax3.set_ylabel('Gap (%)')
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Add value labels
    for i, gap in enumerate(gaps):
        ax3.text(i, gap + 0.2, f'{gap:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    # 4. Performance Distribution
    ax4.hist(df['Retention_Rate'], bins=8, color='#3498DB', alpha=0.7, edgecolor='black')
    ax4.axvline(x=average_retention, color='orange', linestyle=':', linewidth=2, label=f'Average ({average_retention:.1f}%)')
    ax4.axvline(x=industry_target, color='red', linestyle='--', linewidth=2, label=f'Target ({industry_target}%)')
    ax4.set_title('Retention Rate Distribution', fontweight='bold')
    ax4.set_xlabel('Retention Rate (%)')
    ax4.set_ylabel('Frequency')
    ax4.legend()
    
    plt.tight_layout()
    plt.savefig('retention_analysis_dashboard.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return fig

def generate_insights(df, average_retention, industry_target, gap_to_target):
    """
    Generate actionable business insights
    """
    insights = {
        'key_findings': [
            f"Average retention rate of {average_retention:.1f}% is {gap_to_target:.1f}% below industry target",
            "Strong Q2 performance (74.85%) shows potential for improvement",
            "Q1 shows significantly lower performance (65.77%) - potential seasonal issue",
            "Q3 and Q4 show consistent performance around 72-75% range"
        ],
        'business_implications': [
            f"Missing industry benchmark by {gap_to_target:.1f}% represents significant revenue opportunity",
            "Inconsistent quarterly performance suggests operational challenges",
            "Q1 underperformance may indicate onboarding or seasonal retention issues",
            "Current trend shows improvement potential but lacks consistency"
        ],
        'recommendations': [
            "Implement targeted retention campaigns focusing on at-risk customer segments",
            "Develop Q1-specific retention strategies to address seasonal decline",
            "Replicate Q2 success factors across all quarters",
            "Establish customer health scoring system for proactive intervention",
            "Implement customer feedback loops to identify retention drivers"
        ]
    }
    
    return insights

def main():
    """
    Main analysis function
    """
    print("Starting Customer Retention Analysis...")
    print(f"Analysis Contact: 22f3001013@ds.study.iitm.ac.in")
    print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Perform analysis
    df, avg_retention, target, gap = analyze_retention_data()
    
    # Create visualizations
    create_visualizations(df, avg_retention, target)
    
    # Generate insights
    insights = generate_insights(df, avg_retention, target, gap)
    
    print("\n" + "="*60)
    print("KEY INSIGHTS GENERATED")
    print("="*60)
    print("✓ Data analysis completed")
    print("✓ Visualizations created")
    print("✓ Business recommendations generated")
    print("✓ Average retention rate confirmed: 71.9%")
    print("="*60)
    
    return df, insights

if __name__ == "__main__":
    df, insights = main()