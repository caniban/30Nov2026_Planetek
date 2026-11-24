import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from PIL import Image

# ---------------------------------------------------------
# 1. PAGE CONFIG & WHITE THEME STYLING
# ---------------------------------------------------------
st.set_page_config(
    page_title="Dr. Muzaffer Can Iban | Planetek Italia Interview",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Base directory so images work seamlessly in Codespaces & Streamlit Cloud
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Custom CSS for crisp white background, modern cards & EO-inspired palette
st.markdown(
    """
    <style>
        /* Force pure white background */
        .stApp {
            background-color: #FFFFFF;
            color: #1E293B;
        }
        [data-testid="stHeader"] {
            background-color: #FFFFFF;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1280px;
        }

        /* Force Radio widget label & options to pure black */
        div[data-testid="stRadio"] > label,
        div[data-testid="stRadio"] > label p,
        div[data-testid="stRadio"] div[role="radiogroup"] label,
        div[data-testid="stRadio"] div[role="radiogroup"] label p,
        div[data-testid="stRadio"] div[role="radiogroup"] span {
            color: #000000 !important;
        }

        /* Hero Header */
        .hero-box {
            background: linear-gradient(135deg, #F8FAFC 0%, #EFF6FF 100%);
            border-left: 6px solid #0B2545;
            border-radius: 10px;
            padding: 1.5rem 2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 10px rgba(11, 37, 69, 0.05);
        }
        .hero-kicker {
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            color: #0077B6;
            margin-bottom: 0.3rem;
        }
        .hero-title {
            font-size: 2rem;
            font-weight: 800;
            color: #0B2545;
            margin: 0;
            line-height: 1.2;
        }
        .hero-subtitle {
            font-size: 1rem;
            color: #475569;
            margin-top: 0.45rem;
            margin-bottom: 0;
        }

        /* Section Banner */
        .section-header {
            border-bottom: 2px solid #E2E8F0;
            padding-bottom: 0.5rem;
            margin-top: 1.2rem;
            margin-bottom: 1rem;
        }
        .section-header h2 {
            color: #0B2545;
            font-size: 1.45rem;
            font-weight: 700;
            margin: 0;
        }
        .section-badge {
            display: inline-block;
            background-color: #E0F2FE;
            color: #0369A1;
            font-size: 0.78rem;
            font-weight: 700;
            padding: 0.2rem 0.65rem;
            border-radius: 999px;
            margin-bottom: 0.4rem;
        }

        /* KPI Insight Cards */
        .kpi-card {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-top: 4px solid #0077B6;
            border-radius: 10px;
            padding: 1rem 1.1rem;
            box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);
            height: 100%;
        }
        .kpi-card.alert {
            border-top-color: #D9534F;
        }
        .kpi-card.success {
            border-top-color: #0D9488;
        }
        .kpi-card.navy {
            border-top-color: #0B2545;
        }
        .kpi-card.amber {
            border-top-color: #D97706;
        }
        .kpi-label {
            font-size: 0.8rem;
            font-weight: 600;
            color: #64748B;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .kpi-value {
            font-size: 1.6rem;
            font-weight: 800;
            color: #0B2545;
            margin: 0.25rem 0;
        }
        .kpi-sub {
            font-size: 0.82rem;
            color: #475569;
        }

        /* Pipeline Flow Strip */
        .pipeline-strip {
            background-color: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 0.85rem 1.2rem;
            font-size: 0.9rem;
            color: #1E293B;
            margin: 0.8rem 0 1.2rem 0;
        }

        /* Insight Callout Box */
        .insight-box {
            background-color: #FFFBEB;
            border-left: 4px solid #D97706;
            border-radius: 6px;
            padding: 0.9rem 1.1rem;
            font-size: 0.92rem;
            color: #334155;
            margin-top: 0.8rem;
        }
        .eo-takeaway {
            background-color: #F0F9FF;
            border: 1px solid #BAE6FD;
            border-left: 5px solid #0284C7;
            border-radius: 8px;
            padding: 1rem 1.25rem;
            margin-top: 1.2rem;
            color: #0F172A;
            font-size: 0.93rem;
        }

        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            border-bottom: 1px solid #E2E8F0;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: #F8FAFC;
            border-radius: 8px 8px 0 0;
            padding: 0.6rem 1.1rem;
            font-weight: 600;
            color: #475569;
        }
        .stTabs [aria-selected="true"] {
            background-color: #0B2545 !important;
            color: #FFFFFF !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def load_image(filename: str):
    """Safely load an image from the workspace directory."""
    path = os.path.join(BASE_DIR, filename)
    if os.path.exists(path):
        return Image.open(path)
    return None


# ---------------------------------------------------------
# 2. HEADER BANNER
# ---------------------------------------------------------
st.markdown(
    """
    <div class="hero-box">
        <div class="hero-kicker">🛰️ Earth Observation & GeoAI Research Portfolio • Planetek Italia Interview</div>
        <h1 class="hero-title">From Orbit to Actionable Intelligence</h1>
        <p class="hero-subtitle">
            <strong>Dr. Muzaffer Can Iban</strong> &nbsp;|&nbsp; 📍 Bari, Italy &nbsp;|&nbsp; 📅 30 November 2026
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 3. NAVIGATION TABS (5-Tab Structure; Tab 1 Active)
# ---------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🛰️ 1. Post-Earthquake GeoAI (2023–2026)",
        "🌍 2. Module II (Upcoming)",
        "📡 3. Module III (Upcoming)",
        "🗺️ 4. Module IV (Upcoming)",
        "👨‍🔬 5. Vision & Fit (Upcoming)",
    ]
)

# =========================================================
# TAB 1: POST-EARTHQUAKE GEOAI PORTFOLIO (STUDIES 1–4)
# =========================================================
with tab1:
    # Context Banner
    st.markdown(
        """
        <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:0.75rem 1.1rem; margin-bottom:1.2rem; font-size:0.92rem; color:#334155;">
            🌋 <strong>Research Trajectory:</strong> Starting from the <strong>February 6, 2023 Kahramanmaraş Earthquakes</strong> (M<sub>w</sub> 7.8 & 7.6; 50,000+ lives lost, 84,000+ buildings damaged), this 4-study GeoAI progression moves from
            <strong>rapid patch triage (Study 1)</strong> ➡️ <strong>building-level YOLO localization (Study 2)</strong> ➡️ <strong>national building segmentation benchmark (Study 3)</strong> ➡️ <strong>proactive synthetic disaster generation & XAI for Istanbul (Study 4)</strong>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =====================================================
    # STUDY 1: SCENE CLASSIFICATION
    # =====================================================
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">STUDY 1 • PATCH-LEVEL RAPID SCREENING</span>
            <h2>🧩 Two-Stage Deep Learning Scene Classification (Antakya & Iskenderun)</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "Rather than relying solely on compute-heavy pixel segmentation or bounding-box labeling, this study introduces a **practical, fully automated two-stage scene classification pipeline**. "
        "First, **Classifier #1** filters out non-urban land cover by detecting building presence within Maxar VHR image patches. "
        "Next, **Classifier #2** categorizes urban patches into **collapsed** vs. **non-collapsed** scenes—enabling rapid city-wide damage mapping across Antakya and Iskenderun."
    )

    st.markdown(
        """
        <div class="pipeline-strip">
            <strong>⚡ Automated Workflow:</strong> &nbsp;
            🛰️ Maxar VHR Imagery &nbsp;➡️&nbsp;
            🧱 <strong>Classifier #1 (ResNet-101)</strong>: Urban / Building Filter (99.17% Acc.) &nbsp;➡️&nbsp;
            🏚️ <strong>Classifier #2 (DenseNet-121)</strong>: Collapse Detection (93.33% Acc.) &nbsp;➡️&nbsp;
            🗺️ City-Wide Damage Inventory
        </div>
        """,
        unsafe_allow_html=True,
    )

    # KPI Cards — Study 1
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown(
            """
            <div class="kpi-card success">
                <div class="kpi-label">🏛️ Classifier #1 Best</div>
                <div class="kpi-value">99.17%</div>
                <div class="kpi-sub"><strong>ResNet-101</strong> • F1: 0.9916 (Building Presence)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with k2:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">🏚️ Classifier #2 Best</div>
                <div class="kpi-value">93.33%</div>
                <div class="kpi-sub"><strong>DenseNet-121</strong> • Precision: 1.0000 (Collapse)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with k3:
        st.markdown(
            """
            <div class="kpi-card alert">
                <div class="kpi-label">📍 Antakya Collapsed</div>
                <div class="kpi-value">449 <span style="font-size:1rem; color:#64748B;">/ 2,878</span></div>
                <div class="kpi-sub"><strong>15.6%</strong> of urban scenes (2,429 non-collapsed)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with k4:
        st.markdown(
            """
            <div class="kpi-card navy">
                <div class="kpi-label">📍 Iskenderun Collapsed</div>
                <div class="kpi-value">290 <span style="font-size:1rem; color:#64748B;">/ 2,581</span></div>
                <div class="kpi-sub"><strong>11.2%</strong> of urban scenes (2,291 non-collapsed)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # Metrics Data — Study 1
    metrics_data = [
        ("Classifier #1", "DenseNet-121", 0.9583, 0.9167, 1.0000, 0.9565),
        ("Classifier #1", "DenseNet-169", 0.9167, 0.8333, 1.0000, 0.9091),
        ("Classifier #1", "MobileNetv2", 0.9750, 0.9500, 1.0000, 0.9744),
        ("Classifier #1", "ResNet-50", 0.9333, 0.8667, 1.0000, 0.9286),
        ("Classifier #1", "ResNet-50v2", 0.9583, 0.9167, 1.0000, 0.9565),
        ("Classifier #1", "ResNet-101", 0.9917, 0.9833, 1.0000, 0.9916),
        ("Classifier #1", "VGG-16", 0.8750, 0.7833, 0.9592, 0.8624),
        ("Classifier #1", "VGG-19", 0.8833, 0.7833, 0.9792, 0.8704),
        ("Classifier #2", "DenseNet-121", 0.9333, 1.0000, 0.8824, 0.9375),
        ("Classifier #2", "DenseNet-169", 0.8833, 1.0000, 0.8108, 0.8955),
        ("Classifier #2", "MobileNetv2", 0.7000, 1.0000, 0.6250, 0.7692),
        ("Classifier #2", "ResNet-50", 0.7750, 0.7667, 0.7797, 0.7731),
        ("Classifier #2", "ResNet-50v2", 0.9000, 0.9500, 0.8636, 0.9048),
        ("Classifier #2", "ResNet-101", 0.7500, 0.5833, 0.8750, 0.7000),
        ("Classifier #2", "VGG-16", 0.8750, 1.0000, 0.8000, 0.8889),
        ("Classifier #2", "VGG-19", 0.8583, 0.9833, 0.7867, 0.8741),
    ]
    df_metrics = pd.DataFrame(
        metrics_data,
        columns=["Classifier", "Architecture", "Accuracy", "Precision", "Recall", "F-1 Score"],
    )

    col_chart, col_table = st.columns([1.15, 1], gap="large")

    with col_chart:
        selected_clf = st.radio(
            "Select Stage to Inspect Architecture Benchmark:",
            ["Classifier #1 (Building Presence)", "Classifier #2 (Collapsed vs. Non-Collapsed)"],
            horizontal=True,
        )
        clf_key = "Classifier #1" if "Classifier #1" in selected_clf else "Classifier #2"
        df_sub = df_metrics[df_metrics["Classifier"] == clf_key].sort_values("F-1 Score", ascending=True)

        best_arch = df_sub.iloc[-1]["Architecture"]
        colors = ["#0077B6" if arch == best_arch else "#CBD5E1" for arch in df_sub["Architecture"]]

        fig_bench = go.Figure()
        fig_bench.add_trace(
            go.Bar(
                y=df_sub["Architecture"],
                x=df_sub["F-1 Score"],
                orientation="h",
                marker_color=colors,
                text=[f"{v:.4f}" for v in df_sub["F-1 Score"]],
                textposition="outside",
                textfont=dict(color="#000000"),
                name="F-1 Score",
                hovertemplate="<b>%{y}</b><br>F-1 Score: %{x:.4f}<extra></extra>",
            )
        )
        fig_bench.update_layout(
            title=dict(text=f"{clf_key} — F-1 Score Comparison (Top: {best_arch})", font=dict(size=14, color="#0B2545")),
            font=dict(color="#000000"),
            xaxis=dict(
                range=[0.55, 1.08],
                title=dict(text="F-1 Score", font=dict(color="#000000")),
                tickfont=dict(color="#000000"),
                showgrid=True,
                gridcolor="#F1F5F9",
            ),
            yaxis=dict(
                title=dict(text="Architecture", font=dict(color="#000000")),
                tickfont=dict(color="#000000"),
            ),
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            height=330,
            margin=dict(l=10, r=30, t=40, b=30),
        )
        st.plotly_chart(fig_bench, use_container_width=True)

    with col_table:
        st.markdown(f"**📊 Detailed Test Metrics — {clf_key}**")
        display_df = (
            df_metrics[df_metrics["Classifier"] == clf_key]
            .drop(columns=["Classifier"])
            .sort_values("F-1 Score", ascending=False)
            .reset_index(drop=True)
        )

        def highlight_top(row):
            if row.name == 0:
                return ["background-color: #E0F2FE; font-weight: 700; color: #0B2545"] * len(row)
            return [""] * len(row)

        st.dataframe(
            display_df.style.apply(highlight_top, axis=1).format(
                {"Accuracy": "{:.4f}", "Precision": "{:.4f}", "Recall": "{:.4f}", "F-1 Score": "{:.4f}"}
            ),
            use_container_width=True,
            hide_index=True,
            height=315,
        )

    # City-wide Distribution Mini-Chart
    df_city = pd.DataFrame(
        {
            "City": ["Antakya", "Antakya", "Iskenderun", "Iskenderun"],
            "Category": ["Collapsed", "Non-Collapsed", "Collapsed", "Non-Collapsed"],
            "Scenes": [449, 2429, 290, 2291],
        }
    )
    fig_city = px.bar(
        df_city,
        y="City",
        x="Scenes",
        color="Category",
        orientation="h",
        barmode="stack",
        text="Scenes",
        color_discrete_map={"Collapsed": "#D9534F", "Non-Collapsed": "#0D9488"},
        title="City-Wide Urban Scene Classification Output (Classifier #2 — DenseNet-121)",
    )
    fig_city.update_layout(
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        font=dict(color="#000000"),
        height=190,
        margin=dict(l=10, r=20, t=38, b=10),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            title="",
            font=dict(color="#000000"),
        ),
        xaxis=dict(
            title=dict(text="Number of Classified Image Patches", font=dict(color="#000000")),
            tickfont=dict(color="#000000"),
            showgrid=True,
            gridcolor="#F1F5F9",
        ),
        yaxis=dict(
            title=dict(text="City", font=dict(color="#000000")),
            tickfont=dict(color="#000000"),
        ),
        title_font=dict(size=13.5, color="#0B2545"),
    )
    st.plotly_chart(fig_city, use_container_width=True)

    # Visual Gallery — Study 1
    st.markdown("**🖼️ Visual Outputs — Scene Classification & Study Splits**")
    sc_col1, sc_col2, sc_col3 = st.columns(3, gap="medium")
    for col, fname, caption in [
        (sc_col1, "scenclass_0.png", "📍 Antakya Study Area: Train, Test & Validation Regions"),
        (sc_col2, "scenclass_1.png", "🧪 Scene Classifier Predictions on Test Patches"),
        (sc_col3, "scenclass_3.png", "🗺️ Antakya City-Wide Urban/Rural & Collapse Map"),
    ]:
        with col:
            img = load_image(fname)
            if img is not None:
                st.image(img, caption=caption, use_container_width=True)
            else:
                st.info(f"Image `{fname}` not found in workspace.")

    st.markdown("---")

    # =====================================================
    # STUDY 2: OBJECT DETECTION
    # =====================================================
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">STUDY 2 • BUILDING-LEVEL LOCALIZATION</span>
            <h2>🎯 Collapsed Building Object Detection with YOLO Models (Antakya City)</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "To move from patch-level screening to **individual building localization**, this study rigorously benchmarked **YOLOv7, YOLOv7x, YOLOv8l, and YOLOv8x** on Maxar VHR satellite imagery over heavily devastated Antakya. "
        "By integrating precise **geographical coordinates** with detections, the pipeline pinpointed **216 collapsed buildings across 28.20 km²**, generating actionable spatial density heatmaps for emergency response."
    )

    d1, d2, d3, d4 = st.columns(4)
    with d1:
        st.markdown(
            """
            <div class="kpi-card success">
                <div class="kpi-label">🏆 Best Architecture</div>
                <div class="kpi-value">0.79 <span style="font-size:0.95rem; color:#64748B;">mAP@.5</span></div>
                <div class="kpi-sub"><strong>YOLOv7</strong> outperformed v7x, v8l & v8x</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with d2:
        st.markdown(
            """
            <div class="kpi-card alert">
                <div class="kpi-label">🏢 Detected Structures</div>
                <div class="kpi-value">216</div>
                <div class="kpi-sub">Individually localized collapsed buildings</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with d3:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">🗺️ Mapped Footprint</div>
                <div class="kpi-value">28.20 <span style="font-size:1rem; color:#64748B;">km²</span></div>
                <div class="kpi-sub">~7.66 collapsed buildings / km² density</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with d4:
        st.markdown(
            """
            <div class="kpi-card navy">
                <div class="kpi-label">🧭 Spatial Integration</div>
                <div class="kpi-value">GIS-Ready</div>
                <div class="kpi-sub">Geo-referenced coordinates & city heatmap</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    st.markdown("**🖼️ Visual Outputs — Individual Detections & Spatial Density Heatmap**")
    od_pad_l, od_col1, od_col2, od_pad_r = st.columns([0.15, 1, 1, 0.15], gap="large")
    with od_col1:
        img_d1 = load_image("detect1.png")
        if img_d1 is not None:
            st.image(img_d1, caption="🎯 Best YOLO Model (YOLOv7): Individual Collapsed Building Detections", use_container_width=True)
        else:
            st.info("Image `detect1.png` not found in workspace.")
    with od_col2:
        img_d2 = load_image("detect2.png")
        if img_d2 is not None:
            st.image(img_d2, caption="🔥 City-Wide Heatmap of Collapsed Buildings across Antakya (28.20 km²)", use_container_width=True)
        else:
            st.info("Image `detect2.png` not found in workspace.")

    st.markdown(
        """
        <div class="insight-box">
            ⚠️ <strong>Key Operational Challenges:</strong>
            Object detection models can occasionally misclassify non-building structures (rubble piles, vehicles, shadowed infrastructure), and generalizability remains <strong>context-specific</strong> to regional urban morphology—motivating the national benchmark dataset in Study 3.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # =====================================================
    # STUDY 3: GEOAI-RESPOND BUILDING SEGMENTATION DATASET
    # =====================================================
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">STUDY 3 • NATIONAL BENCHMARK DATASET</span>
            <h2>🏗️ GeoAI-RESPOND: Türkiye's First Spatially-Buffered Building Segmentation Dataset</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "**Why is it original?** Global building datasets (*ISPRS, INRIA, SpaceNet, WHU*) reflect Western or East Asian urban grids. "
        "**GeoAI-RESPOND** is the first national reference capturing Türkiye's **attached row-house blocks (bitişik nizam)**, irregular urban fabrics, and regional roof typologies—built directly from **Maxar 3-band RGB** imagery at native **256×256 px (~89.6 m)** resolution with **zero resizing**."
    )

    # KPI Cards — Study 3
    s3_1, s3_2, s3_3, s3_4 = st.columns(4)
    with s3_1:
        st.markdown(
            """
            <div class="kpi-card navy">
                <div class="kpi-label">🧩 Dataset Scale</div>
                <div class="kpi-value">18,656 <span style="font-size:0.95rem; color:#64748B;">tiles</span></div>
                <div class="kpi-sub">17,640 buffered benchmark tiles • 142 km² • 0.35 m GSD</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s3_2:
        st.markdown(
            """
            <div class="kpi-card success">
                <div class="kpi-label">🥇 #1 Transformer</div>
                <div class="kpi-value">85.89 <span style="font-size:0.95rem; color:#64748B;">IoU</span></div>
                <div class="kpi-sub"><strong>Mask2Former-SwinS</strong> (Overall Leader)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s3_3:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">🏛️ Classic Leader</div>
                <div class="kpi-value">84.86 <span style="font-size:0.95rem; color:#64748B;">IoU</span></div>
                <div class="kpi-sub"><strong>DeepLabV3+-R50</strong> (Strong CNN Baseline)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s3_4:
        st.markdown(
            """
            <div class="kpi-card amber">
                <div class="kpi-label">⚡ Lightweight Leader</div>
                <div class="kpi-value">82.57 <span style="font-size:0.95rem; color:#64748B;">IoU</span></div>
                <div class="kpi-sub"><strong>PIDNet-L</strong> (Fast Edge / Rapid Inference)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # Literature Comparison Table + Methodological Edge
    lit_col, iou_col = st.columns([1.25, 1], gap="large")

    with lit_col:
        st.markdown("**📚 Comparison with Global Building Segmentation Benchmarks**")
        df_lit = pd.DataFrame(
            [
                ("INRIA", "0.30 m", "360", "810 km²", "City-based"),
                ("Massachusetts", "1.00 m", "151", "340 km²", "Random"),
                ("WHU-Aerial", "0.30 m", "8,189", "450 km²", "Contiguous area"),
                ("SpaceNet-2", "0.30 m", "24,586", "983 km²", "Random"),
                ("GeoAI-RESPOND (Ours)", "0.35 m", "17,640", "142 km²", "Buffer + Block (≥150 m)"),
            ],
            columns=["Dataset", "GSD", "Tiles", "Coverage", "Split Strategy"],
        )

        def highlight_ours(row):
            if "GeoAI-RESPOND" in row["Dataset"]:
                return ["background-color: #E0F2FE; font-weight: 700; color: #0B2545"] * len(row)
            return [""] * len(row)

        st.dataframe(df_lit.style.apply(highlight_ours, axis=1), use_container_width=True, hide_index=True, height=215)

        st.markdown(
            """
            <div class="insight-box" style="margin-top:0.5rem;">
                🔬 <strong>Methodological Distinction (Anti-Leakage):</strong>
                <em>Massachusetts</em> and <em>SpaceNet-2</em> split randomly (ignoring spatial autocorrelation), while <em>INRIA</em> splits by city (unable to measure intra-fabric generalization). <strong>GeoAI-RESPOND</strong> is the first national dataset guaranteeing a <strong>≥150 m physical buffer</strong> between train/val/test blocks.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with iou_col:
        df_seg_leaders = pd.DataFrame(
            {
                "Model": ["PIDNet-L (Lightweight)", "DeepLabV3+-R50 (Classic)", "Mask2Former-SwinS (Transformer)"],
                "Building IoU (%)": [82.57, 84.86, 85.89],
                "Color": ["#D97706", "#0077B6", "#0D9488"],
            }
        )
        fig_s3 = go.Figure(
            go.Bar(
                y=df_seg_leaders["Model"],
                x=df_seg_leaders["Building IoU (%)"],
                orientation="h",
                marker_color=df_seg_leaders["Color"],
                text=[f"{v:.2f}%" for v in df_seg_leaders["Building IoU (%)"]],
                textposition="outside",
                textfont=dict(color="#000000"),
            )
        )
        fig_s3.update_layout(
            title=dict(text="Top Building Segmentation Models by Family (IoU %)", font=dict(size=14, color="#0B2545")),
            font=dict(color="#000000"),
            xaxis=dict(
                range=[75, 92],
                title=dict(text="Overall Building IoU (%)", font=dict(color="#000000")),
                tickfont=dict(color="#000000"),
                showgrid=True,
                gridcolor="#F1F5F9",
            ),
            yaxis=dict(
                title=dict(text="Architecture Family", font=dict(color="#000000")),
                tickfont=dict(color="#000000"),
            ),
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            height=290,
            margin=dict(l=10, r=35, t=40, b=30),
        )
        st.plotly_chart(fig_s3, use_container_width=True)

    # Visual Gallery — Study 3 (2x2 compact grid)
    st.markdown("**🖼️ Visual Outputs — Labeling, Buffered Splits & Segmentation Predictions**")
    b_r1c1, b_r1c2 = st.columns(2, gap="medium")
    with b_r1c1:
        img = load_image("bina1.png")
        if img is not None:
            st.image(img, caption="🏷️ Building Labeling Across Earthquake-Affected Turkish Cities", use_container_width=True)
        else:
            st.info("Image `bina1.png` not found in workspace.")
    with b_r1c2:
        img = load_image("bina2.png")
        if img is not None:
            st.image(img, caption="🛡️ Buffered Block-Based Train / Validation / Test Split (≥150 m Separation)", use_container_width=True)
        else:
            st.info("Image `bina2.png` not found in workspace.")

    b_r2c1, b_r2c2 = st.columns(2, gap="medium")
    with b_r2c1:
        img = load_image("bina3.png")
        if img is not None:
            st.image(img, caption="📊 Segmentation Performance Across Selected Deep Learning Architectures", use_container_width=True)
        else:
            st.info("Image `bina3.png` not found in workspace.")
    with b_r2c2:
        img = load_image("bina4.png")
        if img is not None:
            st.image(img, caption="🔍 Ground Truth vs. Predicted Building Boundary Overlay Comparison", use_container_width=True)
        else:
            st.info("Image `bina4.png` not found in workspace.")

    st.markdown("---")

    # =====================================================
    # STUDY 4: SYNTHETIC DISASTER GENERATION & XAI FOR ISTANBUL
    # =====================================================
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">STUDY 4 • PROACTIVE PREPAREDNESS & GENERATIVE GEOAI</span>
            <h2>🌊 Synthetic Earthquake & Flood Generation (CycleGAN), Cross-Domain Segmentation & PYLON XAI for Istanbul</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "Building on Study 3's building-footprint foundation, Study 4 addresses a critical pre-disaster challenge: **how do we train damage-assessment models for Istanbul—a megacity awaiting a major earthquake—before disaster strikes?** "
        "We curated **10,000 multi-sensor VHR tiles (5,000 Feb 6 Earthquake Zone + 5,000 Istanbul)** with building, damage-grade, and road-network labels, then trained **CycleGAN** to transfer real Eastern Anatolia collapse patterns and **5% / 10% / 20% secondary flood scenarios** directly onto Istanbul's urban fabric."
    )

    # KPI Cards — Study 4
    s4_1, s4_2, s4_3, s4_4 = st.columns(4)
    with s4_1:
        st.markdown(
            """
            <div class="kpi-card navy">
                <div class="kpi-label">🛰️ Multi-Sensor Archive</div>
                <div class="kpi-value">10,000 <span style="font-size:0.95rem; color:#64748B;">tiles</span></div>
                <div class="kpi-sub">5K Feb 6 + 5K Istanbul • 655.36M labeled pixels</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s4_2:
        st.markdown(
            """
            <div class="kpi-card success">
                <div class="kpi-label">🌍 Cross-Domain F1</div>
                <div class="kpi-value">82.4%</div>
                <div class="kpi-sub">Feb 6 ➡️ Istanbul (Exceeded <strong>80%</strong> target)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s4_3:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">🎨 Generative Scenarios</div>
                <div class="kpi-value">CycleGAN</div>
                <div class="kpi-sub">3 collapse grades + road blockage + 5/10/20% floods</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s4_4:
        st.markdown(
            """
            <div class="kpi-card amber">
                <div class="kpi-label">🔎 PYLON XAI Accuracy</div>
                <div class="kpi-value">2.24 <span style="font-size:0.95rem; color:#64748B;">px</span></div>
                <div class="kpi-sub">Mean center error • <strong>78.6%</strong> spatial overlap</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # Multi-Sensor Inventory & Class Distribution Tables
    inv_col, dist_col = st.columns([1.05, 1], gap="large")
    with inv_col:
        st.markdown("**🛰️ Table 1 — Multi-Sensor VHR Dataset Inventory (256×256 px)**")
        df_inv = pd.DataFrame(
            [
                ("KATE-CD", "Satellite", "Feb 6 Earthquake Zone", "0.30–0.50 m", "1,944"),
                ("Airbus-Maxar", "Satellite", "Feb 6 Earthquake Zone", "0.30–0.50 m", "3,056"),
                ("Pléiades", "Satellite", "Istanbul (Sarıyer, Beykoz, Üsküdar)", "0.30–0.50 m", "3,612"),
                ("Istanbul Metro. Mun.", "Aerial Photo", "Istanbul (Esenler, Bağcılar)", "0.05–0.15 m", "1,388"),
            ],
            columns=["Source", "Type", "Region", "GSD", "Tiles"],
        )
        st.dataframe(df_inv, use_container_width=True, hide_index=True, height=180)

    with dist_col:
        dist_choice = st.radio(
            "Inspect Pixel Class Distribution (327.68M px each):",
            ["Feb 6 Earthquake Zone (7 Classes)", "Istanbul Pre-Disaster (3 Classes)"],
            horizontal=True,
        )
        if "Feb 6" in dist_choice:
            df_dist = pd.DataFrame(
                [
                    (0, "Background", "58.90%", "193,003,520"),
                    (1, "Road (Open)", "11.88%", "38,928,384"),
                    (2, "Damaged / Blocked Road", "1.62%", "5,308,416"),
                    (3, "Undamaged Building", "25.68%", "84,148,224"),
                    (4, "Slight Damage Building", "0.7104%", "2,327,839"),
                    (5, "Major Damage Building", "0.8064%", "2,642,411"),
                    (6, "Complete Damage Building", "0.4032%", "1,321,206"),
                ],
                columns=["ID", "Class", "Share", "Pixels"],
            )
        else:
            df_dist = pd.DataFrame(
                [
                    (0, "Background", "43.47%", "142,442,496"),
                    (1, "Building", "41.53%", "136,085,504"),
                    (2, "Road", "15.00%", "49,152,000"),
                ],
                columns=["ID", "Class", "Share", "Pixels"],
            )
        st.dataframe(df_dist, use_container_width=True, hide_index=True, height=180)

    st.write("")

    # Interactive Segmentation Benchmark (WP-3.1, WP-3.2, WP-3.3)
    st.markdown("**📊 Semantic Segmentation Benchmarks — In-Domain, Cross-Domain & 7-Class Damage**")
    wp_choice = st.radio(
        "Select Experiment Protocol:",
        [
            "WP-3.1 vs WP-3.2 (Domain Shift: Istanbul → Istanbul vs. Feb 6 → Istanbul)",
            "WP-3.3 (Feb 6 Earthquake Zone — 7-Class Building Damage & Road Network)",
        ],
        horizontal=True,
    )

    if "WP-3.1" in wp_choice:
        wp_c1, wp_c2 = st.columns([1.2, 1], gap="large")
        with wp_c1:
            df_shift = pd.DataFrame(
                {
                    "Class": ["Background", "Building", "Road", "Mean", "Background", "Building", "Road", "Mean"],
                    "Scenario": [
                        "WP-3.1 (Istanbul → Istanbul)",
                        "WP-3.1 (Istanbul → Istanbul)",
                        "WP-3.1 (Istanbul → Istanbul)",
                        "WP-3.1 (Istanbul → Istanbul)",
                        "WP-3.2 (Feb 6 → Istanbul)",
                        "WP-3.2 (Feb 6 → Istanbul)",
                        "WP-3.2 (Feb 6 → Istanbul)",
                        "WP-3.2 (Feb 6 → Istanbul)",
                    ],
                    "F-1 Score (%)": [94.1, 90.4, 87.2, 90.6, 89.2, 81.7, 76.3, 82.4],
                }
            )
            fig_shift = px.bar(
                df_shift,
                x="Class",
                y="F-1 Score (%)",
                color="Scenario",
                barmode="group",
                text="F-1 Score (%)",
                color_discrete_map={
                    "WP-3.1 (Istanbul → Istanbul)": "#0D9488",
                    "WP-3.2 (Feb 6 → Istanbul)": "#0077B6",
                },
                title="Domain Shift Impact on F-1 Score (Mean IoU: 82.9% → 70.4%)",
            )
            fig_shift.update_traces(texttemplate="%{text:.1f}%", textposition="outside", textfont=dict(color="#000000"))
            fig_shift.update_layout(
                plot_bgcolor="#FFFFFF",
                paper_bgcolor="#FFFFFF",
                font=dict(color="#000000"),
                height=330,
                margin=dict(l=10, r=20, t=45, b=30),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title="", font=dict(color="#000000")),
                xaxis=dict(title=dict(text="Class", font=dict(color="#000000")), tickfont=dict(color="#000000")),
                yaxis=dict(
                    range=[60, 102],
                    title=dict(text="F-1 Score (%)", font=dict(color="#000000")),
                    tickfont=dict(color="#000000"),
                    showgrid=True,
                    gridcolor="#F1F5F9",
                ),
                title_font=dict(size=13.5, color="#0B2545"),
            )
            st.plotly_chart(fig_shift, use_container_width=True)

        with wp_c2:
            df_wp_tab = pd.DataFrame(
                [
                    ("Background", "93.8 / 94.5 / 94.1", "88.4 / 90.1 / 89.2", "-4.9 pp"),
                    ("Building", "89.7 / 91.2 / 90.4", "79.6 / 84.0 / 81.7", "-8.7 pp"),
                    ("Road", "86.4 / 88.1 / 87.2", "74.1 / 78.6 / 76.3", "-10.9 pp"),
                    ("Mean", "89.9 / 91.3 / 90.6", "80.7 / 84.2 / 82.4", "-8.2 pp"),
                ],
                columns=["Class", "WP-3.1 (P / R / F1 %)", "WP-3.2 (P / R / F1 %)", "F1 Shift"],
            )
            st.markdown("**📋 Precision / Recall / F-1 Comparison**")
            st.dataframe(df_wp_tab, use_container_width=True, hide_index=True, height=180)
            st.markdown(
                """
                <div class="insight-box" style="margin-top:0.5rem;">
                    🛣️ <strong>Domain-Shift Insight:</strong> Cross-region generalization reached <strong>82.4% F1</strong> (surpassing the 80% project target). <strong>Roads</strong> suffered the steepest drop (F1: 87.2% → 76.3%; IoU: 77.3% → 61.7%) due to narrow linear geometry, tree/vehicle occlusions, and multi-sensor radiometric differences.
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        wp3_c1, wp3_c2 = st.columns([1.2, 1], gap="large")
        df_wp33 = pd.DataFrame(
            [
                ("Background", 94.1, 92.9, 93.5),
                ("Undamaged Building", 89.4, 87.6, 88.5),
                ("Road (Open)", 86.1, 83.9, 85.0),
                ("Complete Damage Bldg", 76.8, 71.4, 74.0),
                ("Damaged / Blocked Road", 70.9, 65.3, 68.0),
                ("Major Damage Bldg", 68.7, 63.5, 66.0),
                ("Slight Damage Bldg", 61.2, 55.1, 58.0),
            ],
            columns=["Class", "Precision (%)", "Recall (%)", "F-1 Score (%)"],
        )
        with wp3_c1:
            df_wp33_sorted = df_wp33.sort_values("F-1 Score (%)", ascending=True)
            bar_colors = [
                "#D9534F" if "Damage" in c else "#0077B6" for c in df_wp33_sorted["Class"]
            ]
            fig_wp33 = go.Figure(
                go.Bar(
                    y=df_wp33_sorted["Class"],
                    x=df_wp33_sorted["F-1 Score (%)"],
                    orientation="h",
                    marker_color=bar_colors,
                    text=[f"{v:.1f}%" for v in df_wp33_sorted["F-1 Score (%)"]],
                    textposition="outside",
                    textfont=dict(color="#000000"),
                )
            )
            fig_wp33.update_layout(
                title=dict(text="WP-3.3 (Feb 6 Zone) — 7-Class F-1 Score (Mean: 76.1%)", font=dict(size=14, color="#0B2545")),
                font=dict(color="#000000"),
                xaxis=dict(
                    range=[45, 105],
                    title=dict(text="F-1 Score (%)", font=dict(color="#000000")),
                    tickfont=dict(color="#000000"),
                    showgrid=True,
                    gridcolor="#F1F5F9",
                ),
                yaxis=dict(
                    title=dict(text="Semantic Class", font=dict(color="#000000")),
                    tickfont=dict(color="#000000"),
                ),
                plot_bgcolor="#FFFFFF",
                paper_bgcolor="#FFFFFF",
                height=320,
                margin=dict(l=10, r=35, t=40, b=30),
            )
            st.plotly_chart(fig_wp33, use_container_width=True)

        with wp3_c2:
            st.markdown("**📋 WP-3.3 Detailed Metrics (Mean P: 78.2% | R: 74.2% | F1: 76.1%)**")
            st.dataframe(df_wp33, use_container_width=True, hide_index=True, height=280)

    # Visual Gallery — Study 4 (3 balanced columns)
    st.markdown("**🖼️ Visual Outputs — CycleGAN Synthetic Disasters & PYLON Explainable AI**")
    y_col1, y_col2, y_col3 = st.columns(3, gap="medium")
    for col, fname, caption in [
        (
            y_col1,
            "yapay1.png",
            "🏚️ CycleGAN Synthetic Collapse in Istanbul (Light Blue: Slight, Yellow: Major, Red: Complete)",
        ),
        (
            y_col2,
            "yapay2.png",
            "🌊 CycleGAN Synthetic Flood Scenarios in Istanbul (5%, 10% & 20% Secondary Hazard)",
        ),
        (
            y_col3,
            "yapay3.png",
            "🔥 WP-3.2 Segmentation & PYLON XAI Heatmaps on Synthetically Damaged Istanbul Buildings",
        ),
    ]:
        with col:
            img = load_image(fname)
            if img is not None:
                st.image(img, caption=caption, use_container_width=True)
            else:
                st.info(f"Image `{fname}` not found in workspace.")

    # XAI & End-to-End EO Takeaway
    st.markdown(
        """
        <div class="insight-box">
            🔎 <strong>PYLON Explainable AI Findings:</strong>
            PYLON reliably localizes <strong>Major</strong> and <strong>Complete</strong> building damage across synthetic Istanbul scenes, whereas <strong>Slight Damage</strong> (minor roof deformations at 0.30–0.50 m GSD) remains harder to separate from intact structures. Activation centers achieved a <strong>2.24 px</strong> mean point distance and <strong>78.6%</strong> spatial overlap (approaching the 80% project benchmark).
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="eo-takeaway">
            🛰️ <strong>End-to-End EO Portfolio Synthesis (Studies 1–4):</strong>
            Together, these four studies form a complete disaster-management GeoAI stack—combining <strong>rapid scene triage</strong> (93–99% acc.), <strong>geo-referenced YOLO localization</strong> (0.79 mAP@.5), <strong>spatially-buffered national segmentation benchmarks</strong> (85.89% IoU), and <strong>proactive CycleGAN synthetic hazard simulation + XAI</strong> for pre-disaster urban resilience.
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# PLACEHOLDER TABS (To be built next)
# =========================================================
for tab_obj, label in [
    (tab2, "Module II"),
    (tab3, "Module III"),
    (tab4, "Module IV"),
    (tab5, "Vision & Fit for Planetek Italia"),
]:
    with tab_obj:
        st.info(f"🚧 **{label}** will be added in the next iteration.")