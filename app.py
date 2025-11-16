"""
Tennis Match Monte Carlo Simulator - Streamlit Web App v4.1
Web-based interface for tennis match simulation
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from collections import defaultdict
import io
from tennis_simulator_v41 import PlayerProfile, MatchFormat, SetFormat, TiebreakFormat, run_simulations

# Page config
st.set_page_config(
    page_title="Tennis Match Simulator v4.1",
    page_icon="🎾",
    layout="wide"
)

# Title
st.title("🎾 Tennis Match Monte Carlo Simulator v4.1")
st.markdown("### Head-to-Head Match Simulation with Realistic Pressure & Clutch Modeling")

# Sidebar for ATP Top 20 Reference
with st.sidebar:
    st.header("📊 ATP Top 20 Reference")
    st.markdown("""
    **Key Matchups:**
    
    **Sinner vs Alcaraz:**
    - Sinner: 64%, 3.5%, +2
    - Alcaraz: 63%, 4.5%, +3
    
    **Sinner vs Djokovic:**
    - Sinner: 62%, 3.5%, +2
    - Djokovic: 63%, 3.0%, +4
    
    **Alcaraz vs Djokovic:**
    - Alcaraz: 63%, 4.5%, +3
    - Djokovic: 63%, 3.0%, +4
    
    [View Full ATP Top 20 Parameters](https://github.com)
    """)
    
    st.markdown("---")
    st.markdown("""
    **Parameter Ranges:**
    
    **Serve Win %:** 55-75% typical
    - 55-60%: Weak matchup
    - 60-64%: Below avg
    - 64-67%: Average
    - 67-70%: Strong
    - 70%+: Dominant
    
    **Variability:** 2-6% typical
    - 2-3%: Very consistent
    - 3-4%: Consistent
    - 4-5%: Normal
    - 5-6%: Erratic
    
    **Clutch:** -3 to +4 typical
    - +4: Elite (Djokovic)
    - +3: Excellent (Alcaraz)
    - +2: Very good (Sinner)
    - +1: Good (Medvedev)
    - 0: Neutral
    - -1/-2: Weakness
    """)

# Important note about head-to-head parameters
st.info("⚠️ **CRITICAL:** Parameters are MATCHUP-SPECIFIC, not player abilities. "
        "Kyrgios vs #100 ≠ Kyrgios vs Djokovic!")

# Create two columns for player inputs
col1, col2 = st.columns(2)

with col1:
    st.header("Player 1")
    player1_name = st.text_input("Player 1 Name", value="Player 1", key="p1_name")
    st.markdown("**Serve Parameters (Against THIS Opponent)**")
    p1_serve = st.slider("Serve Win % (vs THIS opponent)", 0, 100, 65, 1, key="p1_serve",
                         help="How often P1 wins serve points IN THIS MATCHUP")
    p1_var = st.slider("Serve Variability %", 1.0, 8.0, 4.0, 0.5, key="p1_var",
                       help="2-3%=Consistent, 4-5%=Normal, 5-6%=Erratic")
    p1_clutch = st.slider("Clutch Factor", -5.0, 5.0, 0.0, 0.5, key="p1_clutch",
                          help="+4=Elite, +2=Very good, 0=Neutral, -2=Weakness")

with col2:
    st.header("Player 2")
    player2_name = st.text_input("Player 2 Name", value="Player 2", key="p2_name")
    st.markdown("**Serve Parameters (Against THIS Opponent)**")
    p2_serve = st.slider("Serve Win % (vs THIS opponent)", 0, 100, 65, 1, key="p2_serve",
                         help="How often P2 wins serve points IN THIS MATCHUP")
    p2_var = st.slider("Serve Variability %", 1.0, 8.0, 4.0, 0.5, key="p2_var",
                       help="2-3%=Consistent, 4-5%=Normal, 5-6%=Erratic")
    p2_clutch = st.slider("Clutch Factor", -5.0, 5.0, 0.0, 0.5, key="p2_clutch",
                          help="+4=Elite, +2=Very good, 0=Neutral, -2=Weakness")

# Match Format Configuration
st.header("⚙️ Match Format Configuration")

format_col1, format_col2, format_col3, format_col4 = st.columns(4)

with format_col1:
    st.subheader("Match Length")
    match_length = st.selectbox(
        "Number of Sets",
        options=["Single Set", "Best of 3 Sets", "Best of 5 Sets"],
        index=1
    )
    num_sets = 1 if match_length == "Single Set" else (3 if "Best of 3" in match_length else 5)

with format_col2:
    st.subheader("Set Format")
    set_format_choice = st.selectbox(
        "Set Type",
        options=[
            "Traditional (to 6)",
            "Fast4 (to 4)",
            "Pro Set (to 8)",
            "Short Set from 0-0 (to 4)",
            "Short Set from 2-2 (to 6)"
        ],
        index=0
    )
    
    set_format_map = {
        "Traditional (to 6)": SetFormat.TRADITIONAL,
        "Fast4 (to 4)": SetFormat.FAST4,
        "Pro Set (to 8)": SetFormat.PROSET,
        "Short Set from 0-0 (to 4)": SetFormat.SHORT_ZERO,
        "Short Set from 2-2 (to 6)": SetFormat.SHORT_TWO
    }
    set_format = set_format_map[set_format_choice]

with format_col3:
    st.subheader("Tiebreak Format")
    tiebreak_choice = st.selectbox(
        "Tiebreak Points",
        options=[
            "Slam (7pt regular, 10pt final)",
            "5 Points All Sets",
            "10 Points All Sets",
            "12 Points All Sets"
        ],
        index=0
    )
    
    tiebreak_map = {
        "Slam (7pt regular, 10pt final)": TiebreakFormat.SLAM,
        "5 Points All Sets": TiebreakFormat.FIVE_ALL,
        "10 Points All Sets": TiebreakFormat.TEN_ALL,
        "12 Points All Sets": TiebreakFormat.TWELVE_ALL
    }
    tiebreak_format = tiebreak_map[tiebreak_choice]

with format_col4:
    st.subheader("Scoring Type")
    scoring_choice = st.selectbox(
        "Game Scoring",
        options=["Advantage Scoring", "No-Ad Scoring"],
        index=0
    )
    use_advantage = (scoring_choice == "Advantage Scoring")

# Number of simulations
st.header("🔢 Simulation Settings")
num_sims = st.slider("Number of Simulations", 100, 5000, 500, 100,
                     help="More simulations = more accurate results (but slower)")

# Run simulation button
if st.button("🎾 Run Simulation", type="primary", use_container_width=True):
    # Create player profiles
    player1 = PlayerProfile(
        name=player1_name,
        serve_win_pct=p1_serve,
        serve_variability=p1_var,
        clutch_factor=p1_clutch
    )
    
    player2 = PlayerProfile(
        name=player2_name,
        serve_win_pct=p2_serve,
        serve_variability=p2_var,
        clutch_factor=p2_clutch
    )
    
    # Create match format
    match_format = MatchFormat(
        num_sets=num_sets,
        set_format=set_format,
        tiebreak_format=tiebreak_format,
        use_advantage=use_advantage
    )
    
    # Run simulations with progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    status_text.text(f"Running {num_sims} simulations...")
    
    # Run the simulations
    results = run_simulations(player1, player2, match_format, num_sims)
    
    progress_bar.progress(100)
    status_text.text("✅ Simulation complete!")
    
    # Convert to DataFrame
    df = pd.DataFrame(results)
    
    # Display results
    st.header("📊 Results Summary")
    
    # Win percentages
    p1_wins = (df['winner'] == player1_name).sum()
    p2_wins = (df['winner'] == player2_name).sum()
    p1_pct = (p1_wins / num_sims) * 100
    p2_pct = (p2_wins / num_sims) * 100
    
    # Display as metrics
    metric_col1, metric_col2 = st.columns(2)
    with metric_col1:
        st.metric(f"{player1_name} Wins", f"{p1_wins}/{num_sims}", f"{p1_pct:.1f}%")
    with metric_col2:
        st.metric(f"{player2_name} Wins", f"{p2_wins}/{num_sims}", f"{p2_pct:.1f}%")
    
    # Average statistics
    st.subheader("Average Match Statistics")
    
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    
    with stat_col1:
        st.metric("Avg Games", f"{df['total_games'].mean():.1f}")
    with stat_col2:
        st.metric("Avg Points", f"{df['total_points'].mean():.0f}")
    with stat_col3:
        avg_bp_conv = (df['p1_bp_converted'].sum() + df['p2_bp_converted'].sum()) / \
                      (df['p1_bp_opportunities'].sum() + df['p2_bp_opportunities'].sum()) * 100
        st.metric("Avg BP Conversion", f"{avg_bp_conv:.1f}%")
    with stat_col4:
        tiebreak_pct = (df['set1_score'].str.contains('7-6|6-7', regex=True).sum() + \
                       df['set2_score'].str.contains('7-6|6-7', regex=True).fillna(False).sum() + \
                       df['set3_score'].str.contains('7-6|6-7', regex=True).fillna(False).sum()) / \
                       (num_sims * num_sets) * 100
        st.metric("Tiebreak Frequency", f"{tiebreak_pct:.1f}%")
    
    # Player-specific statistics
    st.subheader(f"📈 {player1_name} Statistics")
    p1_stats_col1, p1_stats_col2, p1_stats_col3, p1_stats_col4 = st.columns(4)
    
    with p1_stats_col1:
        st.metric("Avg Serve Win %", f"{df['p1_serve_pct'].mean():.1f}%")
    with p1_stats_col2:
        st.metric("Avg Games Won", f"{df['p1_games'].mean():.1f}")
    with p1_stats_col3:
        p1_bp_save = df['p1_bp_saved'].sum() / df['p1_bp_faced'].sum() * 100 if df['p1_bp_faced'].sum() > 0 else 0
        st.metric("BP Save %", f"{p1_bp_save:.1f}%")
    with p1_stats_col4:
        p1_bp_conv = df['p1_bp_converted'].sum() / df['p1_bp_opportunities'].sum() * 100 if df['p1_bp_opportunities'].sum() > 0 else 0
        st.metric("BP Conversion %", f"{p1_bp_conv:.1f}%")
    
    st.subheader(f"📈 {player2_name} Statistics")
    p2_stats_col1, p2_stats_col2, p2_stats_col3, p2_stats_col4 = st.columns(4)
    
    with p2_stats_col1:
        st.metric("Avg Serve Win %", f"{df['p2_serve_pct'].mean():.1f}%")
    with p2_stats_col2:
        st.metric("Avg Games Won", f"{df['p2_games'].mean():.1f}")
    with p2_stats_col3:
        p2_bp_save = df['p2_bp_saved'].sum() / df['p2_bp_faced'].sum() * 100 if df['p2_bp_faced'].sum() > 0 else 0
        st.metric("BP Save %", f"{p2_bp_save:.1f}%")
    with p2_stats_col4:
        p2_bp_conv = df['p2_bp_converted'].sum() / df['p2_bp_opportunities'].sum() * 100 if df['p2_bp_opportunities'].sum() > 0 else 0
        st.metric("BP Conversion %", f"{p2_bp_conv:.1f}%")
    
    # Download buttons
    st.header("💾 Download Results")
    
    download_col1, download_col2 = st.columns(2)
    
    with download_col1:
        # CSV download
        csv = df.to_csv(index=False)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"tennis_sim_{player1_name}_vs_{player2_name}_{timestamp}.csv"
        
        st.download_button(
            label="📄 Download CSV Results",
            data=csv,
            file_name=filename,
            mime="text/csv",
            use_container_width=True
        )
    
    with download_col2:
        # Generate summary text
        summary_lines = []
        summary_lines.append("=" * 80)
        summary_lines.append("TENNIS MATCH SIMULATION SUMMARY")
        summary_lines.append("=" * 80)
        summary_lines.append(f"\nSimulation Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        summary_lines.append(f"Number of Simulations: {num_sims}")
        summary_lines.append(f"\nMatch Format: {match_length}, {set_format_choice}, {tiebreak_choice}, {scoring_choice}")
        summary_lines.append("\n" + "=" * 80)
        summary_lines.append("PLAYER PARAMETERS (HEAD-TO-HEAD MATCHUP)")
        summary_lines.append("=" * 80)
        summary_lines.append(f"\n{player1_name}:")
        summary_lines.append(f"  Serve Win %: {p1_serve}%")
        summary_lines.append(f"  Variability: {p1_var}%")
        summary_lines.append(f"  Clutch Factor: {p1_clutch:+.1f}")
        summary_lines.append(f"\n{player2_name}:")
        summary_lines.append(f"  Serve Win %: {p2_serve}%")
        summary_lines.append(f"  Variability: {p2_var}%")
        summary_lines.append(f"  Clutch Factor: {p2_clutch:+.1f}")
        summary_lines.append("\n" + "=" * 80)
        summary_lines.append("RESULTS")
        summary_lines.append("=" * 80)
        summary_lines.append(f"\n{player1_name} wins: {p1_wins}/{num_sims} ({p1_pct:.1f}%)")
        summary_lines.append(f"{player2_name} wins: {p2_wins}/{num_sims} ({p2_pct:.1f}%)")
        summary_lines.append(f"\nAverage games per match: {df['total_games'].mean():.1f}")
        summary_lines.append(f"Average points per match: {df['total_points'].mean():.0f}")
        summary_lines.append(f"Tiebreak frequency: {tiebreak_pct:.1f}%")
        summary_lines.append(f"Average BP conversion: {avg_bp_conv:.1f}%")
        
        summary_text = "\n".join(summary_lines)
        summary_filename = f"tennis_sim_SUMMARY_{player1_name}_vs_{player2_name}_{timestamp}.txt"
        
        st.download_button(
            label="📝 Download Summary Report",
            data=summary_text,
            file_name=summary_filename,
            mime="text/plain",
            use_container_width=True
        )
    
    # Show sample of results
    st.header("🔍 Sample Results (First 20 Matches)")
    st.dataframe(df.head(20), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p><strong>Tennis Match Monte Carlo Simulator v4.1</strong></p>
    <p>Complete format flexibility with realistic pressure & clutch modeling</p>
    <p>Parameters are HEAD-TO-HEAD matchup specific, not general player abilities</p>
</div>
""", unsafe_allow_html=True)
