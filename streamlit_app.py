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
            max-width: 1560px;
        }

        /* Force Radio & Selectbox labels/options to pure black */
        div[data-testid="stRadio"] > label,
        div[data-testid="stRadio"] > label p,
        div[data-testid="stRadio"] div[role="radiogroup"] label,
        div[data-testid="stRadio"] div[role="radiogroup"] label p,
        div[data-testid="stRadio"] div[role="radiogroup"] span,
        div[data-testid="stSelectbox"] > label,
        div[data-testid="stSelectbox"] > label p {
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
            font-size: 2.45rem;
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


@st.cache_data(show_spinner=False)
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
# TAB 1: DISASTER GEOAI (STUDIES 1–3)
# ---------------------------------------------------------
def render_disaster():
    # Context Banner
    st.markdown(
        """
        <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:0.75rem 1.1rem; margin-bottom:1.2rem; font-size:0.92rem; color:#334155;">
            🌋 <strong>Research Trajectory:</strong> Starting from the <strong>February 6, 2023 Kahramanmaraş Earthquakes</strong> (M<sub>w</sub> 7.8 & 7.6; 50,000+ lives lost, 84,000+ buildings damaged), this 3-study GeoAI progression moves from
            <strong>rapid patch triage (Study 1)</strong> ➡️ <strong>building-level YOLO localization (Study 2)</strong> ➡️ <strong>a spatially-buffered national building segmentation benchmark (Study 3)</strong>.
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

    col_chart, col_city = st.columns([1.15, 1], gap="large")

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

    with col_city:
        st.write("")
        st.write("")
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
            height=330,
            margin=dict(l=10, r=20, t=55, b=30),
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
        "**GeoAI-RESPOND** is the first national reference capturing Türkiye's **attached row-house blocks**, irregular urban fabrics, and regional roof typologies—built directly from **Maxar 3-band RGB** imagery at native **256×256 px (~89.6 m)** resolution with **zero resizing**."
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
                ("GeoAI-RESPOND", "0.35 m", "17,640", "142 km²", "Buffer + Block (≥150 m)"),
            ],
            columns=["Dataset", "GSD", "Tiles", "Coverage", "Split Strategy"],
        )

        def highlight_geoai(row):
            if "GeoAI-RESPOND" in row["Dataset"]:
                return ["background-color: #E0F2FE; font-weight: 700; color: #0B2545"] * len(row)
            return [""] * len(row)

        st.dataframe(df_lit.style.apply(highlight_geoai, axis=1), use_container_width=True, hide_index=True, height=215)

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

    # Planetek-Aligned Strategic Takeaway
    st.markdown(
        """
        <div class="eo-takeaway">
            🛰️ <strong>Operational EO Value — Aligned with Planetek Italia Services:</strong>
            This three-tier emergency GeoAI architecture directly mirrors operational Earth Observation service delivery (such as <strong>Copernicus EMS Rapid Mapping</strong> and <strong>Rheticus-style continuous monitoring</strong>):
            <strong>low-compute scene triage</strong> accelerates province-wide situational awareness within hours of VHR acquisition, <strong>geo-referenced YOLO localization</strong> delivers GIS-ready crisis intelligence for civil protection teams, and <strong>spatially-buffered benchmarks (GeoAI-RESPOND)</strong> ensure trustworthy, leakage-free model validation across complex Mediterranean urban fabrics.
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# TAB 2: PALMCITY — 360° PANORAMIC SVI & SEMANTIC SEGMENTATION
# =========================================================
def render_palmcity():
    # Context Banner
    st.markdown(
        """
        <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:0.75rem 1.1rem; margin-bottom:1.2rem; font-size:0.92rem; color:#334155;">
            🌴 <strong>Project Overview (PalmCity):</strong> A local <strong>360° Panoramic Street View Imagery (SVI)</strong> benchmark collected across <strong>Mersin, Türkiye</strong> (4 central districts, 13 field campaigns) using a <strong>GoPro Max 360</strong> (5760×2880 px).
            Unlike perspective-only datasets (<em>Cityscapes, BDD100K</em>) or synthetic panoramas (<em>SynPASS</em>), PalmCity captures authentic Mediterranean urban fabrics—spanning <strong>5 urban typologies</strong> and <strong>32 fine-grained semantic classes</strong>—to power street-level urban analytics and digital twins.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # KPI Cards — PalmCity
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown(
            """
            <div class="kpi-card navy">
                <div class="kpi-label">📷 360° SVI Archive</div>
                <div class="kpi-value">5,232</div>
                <div class="kpi-sub">Geo-tagged panoramas • 13 campaigns • Mapillary-ready</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with p2:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">🏷️ Pixel-Level Labels</div>
                <div class="kpi-value">830 <span style="font-size:0.95rem; color:#64748B;">SVIs</span></div>
                <div class="kpi-sub"><strong>32 semantic classes</strong> annotated in Supervisely</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with p3:
        st.markdown(
            """
            <div class="kpi-card success">
                <div class="kpi-label">🏆 Best of 20 Models</div>
                <div class="kpi-value">0.4915 <span style="font-size:0.95rem; color:#64748B;">mIoU</span></div>
                <div class="kpi-sub"><strong>Mask2Former-SwinS</strong> (mF1: 0.60 • mPrec: 0.69)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with p4:
        st.markdown(
            """
            <div class="kpi-card amber">
                <div class="kpi-label">🏙️ Urban Morphologies</div>
                <div class="kpi-value">5 <span style="font-size:0.95rem; color:#64748B;">typologies</span></div>
                <div class="kpi-sub">Bazaar, Planned Res., Planned Apt., Informal, Coastal</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # -----------------------------------------------------
    # SECTION 2.1: 32 SEMANTIC CLASSES & QUALITATIVE VISUALS FIRST
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">SEMANTIC SCHEMA &amp; QUALITATIVE EVALUATION</span>
            <h2>🖼️ 32-Class Palette &amp; Ground Truth vs. Segmentation Predictions</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    palm_classes_en = [
        (1, "Road", "Flat", "rgb(128, 64, 128)", "#804080"),
        (2, "Sidewalk", "Flat", "rgb(244, 35, 232)", "#F423E8"),
        (3, "Parking Lot", "Flat", "rgb(250, 170, 160)", "#FAAAA0"),
        (4, "Parking Barrier", "Street Furniture", "rgb(255, 129, 0)", "#FF8100"),
        (5, "Soil", "Nature", "rgb(192, 182, 154)", "#C0B69A"),
        (6, "Pedestrian", "Human", "rgb(220, 20, 60)", "#DC143C"),
        (7, "Driver", "Human", "rgb(255, 0, 0)", "#FF0000"),
        (8, "Car", "Vehicle", "rgb(0, 0, 142)", "#00008E"),
        (9, "Truck", "Vehicle", "rgb(0, 0, 70)", "#000046"),
        (10, "Bus", "Vehicle", "rgb(0, 60, 100)", "#003C64"),
        (11, "Motorbike", "Vehicle", "rgb(0, 0, 230)", "#0000E6"),
        (12, "Bicycle", "Vehicle", "rgb(119, 11, 32)", "#770B20"),
        (13, "Traffic Light", "Object", "rgb(250, 170, 30)", "#FAAA1E"),
        (14, "Traffic Sign", "Object", "rgb(220, 220, 0)", "#DCDC00"),
        (15, "Pole", "Object", "rgb(153, 153, 153)", "#999999"),
        (16, "Garbage Box", "Street Furniture", "rgb(137, 145, 169)", "#8991A9"),
        (17, "Sitting Bench", "Street Furniture", "rgb(145, 161, 153)", "#91A199"),
        (18, "Infrastructure Cover", "Infrastructure", "rgb(74, 68, 42)", "#4A442A"),
        (19, "Infrastructure Box", "Infrastructure", "rgb(54, 95, 145)", "#365F91"),
        (20, "Building", "Construction", "rgb(70, 70, 70)", "#464646"),
        (21, "Wall", "Construction", "rgb(102, 102, 156)", "#66669C"),
        (22, "Fence", "Construction", "rgb(190, 153, 153)", "#BE9999"),
        (23, "Guardrail", "Construction", "rgb(180, 165, 180)", "#B4A5B4"),
        (24, "Bridge / Tunnel", "Construction", "rgb(150, 100, 100)", "#966464"),
        (25, "Vegetation / Tree", "Nature", "rgb(107, 142, 35)", "#6B8E23"),
        (26, "Terrain / Grass", "Nature", "rgb(152, 251, 152)", "#98FB98"),
        (27, "Sky", "Sky", "rgb(70, 130, 180)", "#4682B4"),
        (28, "Water Surface", "Nature", "rgb(0, 100, 200)", "#0064C8"),
        (29, "Operator Shadow", "Ego / Special", "rgb(60, 60, 60)", "#3C3C3C"),
        (30, "Operator Body", "Ego / Special", "rgb(40, 40, 40)", "#282828"),
        (31, "Stairs", "Construction", "rgb(200, 200, 150)", "#C8C896"),
        (32, "Void / Unlabeled", "Void", "rgb(0, 0, 0)", "#000000"),
    ]

    with st.expander("🎨 Inspect PalmCity 32 Semantic Classes & RGB Color Palette", expanded=False):
        pal_cols = st.columns(4)
        for idx, (cid, cname, ccat, crgb, chex) in enumerate(palm_classes_en):
            with pal_cols[idx % 4]:
                st.markdown(
                    f"""
                    <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:8px 10px; margin-bottom:8px;">
                        <div style="display:flex; align-items:center; justify-content:space-between;">
                            <span style="font-weight:700; font-size:0.84rem; color:#0B2545;">{cid}. {cname}</span>
                            <span style="background:{chex}; width:18px; height:18px; border-radius:50%; display:inline-block; border:1px solid #94A3B8;"></span>
                        </div>
                        <div style="font-size:0.75rem; color:#64748B; margin-top:2px;">{ccat} • {crgb}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    st.write("")
    pad_l, mid_img, pad_r = st.columns([0.08, 1, 0.08])
    with mid_img:
        img_palm1 = load_image("palm1.png")
        if img_palm1 is not None:
            st.image(
                img_palm1,
                caption="🌴 Qualitative Comparison: Input 360° SVI, Ground Truth Annotations & Semantic Segmentation Predictions on PalmCity",
                use_container_width=True,
            )
        else:
            st.info("Image `palm1.png` not found in workspace (`/workspaces/30Nov2026_Planetek/palm1.png`).")

    st.markdown("---")

    # -----------------------------------------------------
    # SECTION 2.2: 20-MODEL BENCHMARK (BAR CHART ONLY)
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">BENCHMARK • 20 DEEP LEARNING ARCHITECTURES</span>
            <h2>📊 Holistic Semantic Segmentation Ranking on PalmCity (32 Classes)</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    palm_models_data = [
        (1, "Mask2Former-SwinS", "Transformer", 0.69, 0.56, 0.60, 0.4915),
        (2, "SegFormer-B5", "Transformer", 0.70, 0.55, 0.60, 0.4849),
        (3, "SegFormer-B4", "Transformer", 0.69, 0.56, 0.59, 0.4846),
        (4, "SegFormer-B3", "Transformer", 0.72, 0.55, 0.60, 0.4826),
        (5, "FCN-R50", "Classic CNN", 0.66, 0.53, 0.57, 0.4679),
        (6, "FCN-R101", "Classic CNN", 0.65, 0.53, 0.57, 0.4663),
        (7, "Mask2Former-SwinT", "Transformer", 0.65, 0.53, 0.57, 0.4626),
        (8, "DeepLabV3-R50", "Classic CNN", 0.64, 0.53, 0.56, 0.4553),
        (9, "Mask2Former-R101", "Hybrid / CNN-M2F", 0.66, 0.51, 0.56, 0.4496),
        (10, "DeepLabV3+-R50", "Classic CNN", 0.63, 0.53, 0.55, 0.4466),
        (11, "STDC2", "Lightweight", 0.67, 0.50, 0.55, 0.4435),
        (12, "Mask2Former-R50", "Hybrid / CNN-M2F", 0.63, 0.50, 0.53, 0.4326),
        (13, "DeepLabV3-R101", "Classic CNN", 0.63, 0.50, 0.54, 0.4320),
        (14, "DeepLabV3+-R101", "Classic CNN", 0.52, 0.50, 0.51, 0.4188),
        (15, "DDRNet-23", "Lightweight", 0.64, 0.48, 0.52, 0.4155),
        (16, "PSPNet-R50", "Classic CNN", 0.60, 0.49, 0.52, 0.4150),
        (17, "PIDNet-S", "Lightweight", 0.50, 0.48, 0.47, 0.3646),
        (18, "PIDNet-L", "Lightweight", 0.50, 0.48, 0.47, 0.3642),
        (19, "PIDNet-M", "Lightweight", 0.41, 0.47, 0.41, 0.3129),
        (20, "PSPNet-R101", "Classic CNN", 0.44, 0.35, 0.38, 0.2919),
    ]
    df_palm_models = pd.DataFrame(
        palm_models_data,
        columns=["Rank", "Model", "Family", "mPrecision", "mRecall", "mF1-Score", "mIoU"],
    )

    df_plot_pm = df_palm_models.sort_values("mIoU", ascending=True)
    family_colors = {
        "Transformer": "#0D9488",
        "Classic CNN": "#0077B6",
        "Hybrid / CNN-M2F": "#6366F1",
        "Lightweight": "#D97706",
    }
    fig_pm = px.bar(
        df_plot_pm,
        y="Model",
        x="mIoU",
        color="Family",
        orientation="h",
        text=df_plot_pm["mIoU"].map(lambda v: f"{v:.4f}"),
        color_discrete_map=family_colors,
        title="20-Model mIoU Benchmark by Architecture Family",
    )
    fig_pm.update_traces(textposition="outside", textfont=dict(color="#000000", size=11))
    fig_pm.update_layout(
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        font=dict(color="#000000"),
        height=560,
        margin=dict(l=10, r=50, t=55, b=30),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.01,
            xanchor="right",
            x=1,
            title="",
            font=dict(color="#000000"),
        ),
        xaxis=dict(
            range=[0.20, 0.55],
            title=dict(text="Mean IoU (mIoU)", font=dict(color="#000000")),
            tickfont=dict(color="#000000"),
            showgrid=True,
            gridcolor="#F1F5F9",
        ),
        yaxis=dict(
            title=dict(text="Model", font=dict(color="#000000")),
            tickfont=dict(color="#000000"),
        ),
        title_font=dict(size=14, color="#0B2545"),
    )
    st.plotly_chart(fig_pm, use_container_width=True)

    st.markdown(
        """
        <div class="insight-box" style="margin-top:0.2rem;">
            🏆 <strong>Transformer Dominance:</strong> The top 4 spots are held exclusively by <strong>Vision Transformers</strong> (Mask2Former-SwinS &amp; SegFormer B3–B5, 0.4826–0.4915 mIoU), while <strong>STDC2</strong> (0.4435 mIoU) leads the lightweight real-time family.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # -----------------------------------------------------
    # SECTION 2.3: CLASS-WISE IoU BAR CHART (PALETTE-COLORED)
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">FINE-GRAINED DIAGNOSTICS • 32 SEMANTIC CLASSES</span>
            <h2>🔬 Class-Wise IoU Performance Across All 20 Architectures</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    model_cols = [
        "FCN50", "FCN101", "PSP50", "PSP101", "DLv3-50", "DLv3-101", "DLv3+50", "DLv3+101",
        "DDR23", "PID-S", "PID-M", "PID-L", "STDC2", "SF-B3", "SF-B4", "SF-B5",
        "M2F-R50", "M2F-R101", "M2F-ST", "M2F-SS",
    ]

    class_iou_rows = [
        ("Road", [0.93, 0.94, 0.89, 0.88, 0.93, 0.92, 0.94, 0.94, 0.93, 0.89, 0.81, 0.89, 0.93, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94]),
        ("Sidewalk", [0.73, 0.75, 0.52, 0.49, 0.74, 0.72, 0.78, 0.76, 0.71, 0.60, 0.46, 0.61, 0.73, 0.79, 0.79, 0.76, 0.75, 0.76, 0.75, 0.77]),
        ("Parking lot", [0.06, 0.10, 0.15, 0.04, 0.20, 0.12, 0.07, 0.13, 0.05, 0.05, 0.08, 0.05, 0.06, 0.09, 0.05, 0.05, 0.05, 0.05, 0.10, 0.09]),
        ("Soil", [0.65, 0.68, 0.46, 0.41, 0.61, 0.57, 0.64, 0.55, 0.55, 0.51, 0.34, 0.49, 0.66, 0.59, 0.63, 0.59, 0.45, 0.52, 0.56, 0.57]),
        ("Pedestrian", [0.56, 0.55, 0.51, 0.27, 0.51, 0.45, 0.53, 0.53, 0.49, 0.38, 0.33, 0.40, 0.44, 0.58, 0.59, 0.59, 0.58, 0.57, 0.60, 0.61]),
        ("Driver", [0.12, 0.18, 0.24, 0.00, 0.11, 0.05, 0.01, 0.00, 0.11, 0.17, 0.00, 0.17, 0.17, 0.22, 0.14, 0.24, 0.15, 0.21, 0.00, 0.20]),
        ("Car", [0.88, 0.86, 0.84, 0.68, 0.87, 0.85, 0.85, 0.83, 0.83, 0.73, 0.72, 0.75, 0.85, 0.84, 0.87, 0.87, 0.86, 0.86, 0.87, 0.87]),
        ("Truck", [0.31, 0.25, 0.37, 0.09, 0.42, 0.38, 0.41, 0.32, 0.30, 0.30, 0.25, 0.20, 0.25, 0.34, 0.32, 0.34, 0.28, 0.28, 0.28, 0.44]),
        ("Bus", [0.62, 0.63, 0.60, 0.45, 0.61, 0.51, 0.68, 0.63, 0.30, 0.36, 0.03, 0.22, 0.56, 0.44, 0.51, 0.48, 0.53, 0.44, 0.55, 0.71]),
        ("Motorcycle", [0.37, 0.41, 0.31, 0.13, 0.42, 0.38, 0.40, 0.34, 0.36, 0.28, 0.24, 0.31, 0.29, 0.51, 0.52, 0.51, 0.45, 0.48, 0.53, 0.56]),
        ("Bicycle", [0.17, 0.03, 0.06, 0.00, 0.00, 0.04, 0.01, 0.00, 0.03, 0.01, 0.04, 0.04, 0.07, 0.21, 0.20, 0.10, 0.01, 0.16, 0.22, 0.25]),
        ("Traffic Light", [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.04, 0.00, 0.00, 0.18, 0.00, 0.00, 0.01, 0.00, 0.00, 0.00, 0.00]),
        ("Traffic Sign", [0.36, 0.28, 0.21, 0.00, 0.17, 0.08, 0.19, 0.00, 0.03, 0.02, 0.00, 0.04, 0.22, 0.05, 0.06, 0.07, 0.04, 0.12, 0.09, 0.08]),
        ("Pole", [0.48, 0.47, 0.33, 0.25, 0.41, 0.37, 0.45, 0.41, 0.34, 0.25, 0.20, 0.26, 0.40, 0.44, 0.44, 0.44, 0.44, 0.45, 0.46, 0.47]),
        ("Garbage Box", [0.51, 0.51, 0.44, 0.16, 0.47, 0.44, 0.40, 0.37, 0.56, 0.48, 0.42, 0.50, 0.42, 0.64, 0.63, 0.66, 0.56, 0.59, 0.60, 0.61]),
        ("Sitting Bench", [0.36, 0.28, 0.07, 0.00, 0.23, 0.23, 0.17, 0.16, 0.07, 0.04, 0.11, 0.15, 0.26, 0.29, 0.30, 0.29, 0.04, 0.03, 0.21, 0.23]),
        ("Infrastructure Cover", [0.59, 0.65, 0.43, 0.23, 0.55, 0.55, 0.49, 0.46, 0.43, 0.26, 0.21, 0.23, 0.59, 0.52, 0.53, 0.53, 0.48, 0.51, 0.54, 0.53]),
        ("Infrastructure Box", [0.49, 0.52, 0.45, 0.15, 0.48, 0.43, 0.46, 0.44, 0.28, 0.26, 0.20, 0.26, 0.47, 0.37, 0.36, 0.40, 0.28, 0.30, 0.32, 0.38]),
        ("Parking Barrier", [0.39, 0.39, 0.28, 0.24, 0.39, 0.34, 0.47, 0.34, 0.30, 0.23, 0.17, 0.23, 0.31, 0.39, 0.39, 0.40, 0.42, 0.41, 0.40, 0.40]),
        ("Building", [0.93, 0.93, 0.92, 0.87, 0.92, 0.92, 0.93, 0.92, 0.92, 0.88, 0.84, 0.88, 0.92, 0.93, 0.93, 0.93, 0.92, 0.92, 0.93, 0.93]),
        ("Wall", [0.62, 0.63, 0.51, 0.41, 0.59, 0.58, 0.57, 0.54, 0.55, 0.45, 0.39, 0.46, 0.60, 0.60, 0.60, 0.60, 0.55, 0.58, 0.59, 0.60]),
        ("Fence", [0.48, 0.48, 0.39, 0.23, 0.48, 0.41, 0.45, 0.37, 0.52, 0.41, 0.34, 0.42, 0.46, 0.58, 0.57, 0.56, 0.42, 0.46, 0.56, 0.56]),
        ("Stair", [0.06, 0.04, 0.12, 0.00, 0.08, 0.18, 0.13, 0.12, 0.16, 0.12, 0.04, 0.08, 0.05, 0.20, 0.25, 0.24, 0.18, 0.18, 0.14, 0.19]),
        ("Railing", [0.00, 0.00, 0.00, 0.00, 0.01, 0.00, 0.02, 0.00, 0.06, 0.08, 0.06, 0.07, 0.01, 0.23, 0.21, 0.18, 0.16, 0.25, 0.15, 0.26]),
        ("Overpass", [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.15, 0.02, 0.03, 0.01, 0.00, 0.16, 0.14, 0.25, 0.00, 0.00, 0.00, 0.00]),
        ("Water Surface", [0.87, 0.89, 0.81, 0.16, 0.86, 0.81, 0.71, 0.84, 0.83, 0.71, 0.61, 0.72, 0.87, 0.88, 0.87, 0.87, 0.84, 0.86, 0.87, 0.87]),
        ("Sky", [0.99, 0.99, 0.99, 0.98, 0.99, 0.98, 0.99, 0.99, 0.99, 0.98, 0.97, 0.98, 0.98, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99]),
        ("Tree", [0.80, 0.80, 0.76, 0.71, 0.79, 0.77, 0.79, 0.77, 0.80, 0.73, 0.70, 0.73, 0.78, 0.83, 0.83, 0.83, 0.81, 0.80, 0.82, 0.83]),
        ("Grass", [0.57, 0.58, 0.55, 0.51, 0.61, 0.60, 0.62, 0.53, 0.55, 0.45, 0.47, 0.47, 0.54, 0.61, 0.62, 0.60, 0.50, 0.52, 0.56, 0.58]),
        ("Trimmed Tree", [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]),
        ("Void", [0.20, 0.20, 0.16, 0.12, 0.21, 0.20, 0.22, 0.21, 0.20, 0.14, 0.11, 0.17, 0.19, 0.26, 0.28, 0.26, 0.23, 0.23, 0.25, 0.28]),
        ("Operator & Shadow", [0.91, 0.92, 0.91, 0.88, 0.91, 0.92, 0.91, 0.91, 0.92, 0.82, 0.84, 0.87, 0.91, 0.93, 0.93, 0.93, 0.92, 0.92, 0.92, 0.92]),
    ]

    # Exact PalmCity RGB/HEX color map for each semantic class
    class_color_map = {
        "Road": "#804080",
        "Sidewalk": "#F423E8",
        "Parking lot": "#FAAAA0",
        "Parking Barrier": "#FF8100",
        "Soil": "#C0B69A",
        "Pedestrian": "#DC143C",
        "Driver": "#FF0000",
        "Car": "#00008E",
        "Truck": "#000046",
        "Bus": "#003C64",
        "Motorcycle": "#0000E6",
        "Bicycle": "#770B20",
        "Traffic Light": "#FAAA1E",
        "Traffic Sign": "#DCDC00",
        "Pole": "#999999",
        "Garbage Box": "#8991A9",
        "Sitting Bench": "#91A199",
        "Infrastructure Cover": "#4A442A",
        "Infrastructure Box": "#365F91",
        "Building": "#464646",
        "Wall": "#66669C",
        "Fence": "#BE9999",
        "Railing": "#B4A5B4",
        "Overpass": "#966464",
        "Tree": "#6B8E23",
        "Grass": "#98FB98",
        "Trimmed Tree": "#6B8E23",
        "Sky": "#4682B4",
        "Water Surface": "#0064C8",
        "Operator & Shadow": "#3C3C3C",
        "Stair": "#C8C896",
        "Void": "#000000",
    }

    df_class_iou = pd.DataFrame(
        [vals for _, vals in class_iou_rows],
        index=[cls for cls, _ in class_iou_rows],
        columns=model_cols,
    )

    sel_model = st.selectbox(
        "Choose Architecture to Inspect Per-Class IoU (Bars Colored by Official PalmCity Semantic RGB Palette):",
        options=list(reversed(model_cols)),
        index=0,
    )
    s_model = df_class_iou[sel_model].sort_values(ascending=True)
    bar_cols = [class_color_map.get(cls, "#64748B") for cls in s_model.index]

    fig_cls = go.Figure(
        go.Bar(
            y=s_model.index,
            x=s_model.values,
            orientation="h",
            marker=dict(color=bar_cols, line=dict(color="#334155", width=0.7)),
            text=[f"{v:.2f}" for v in s_model.values],
            textposition="outside",
            textfont=dict(color="#000000", size=10.5),
        )
    )
    fig_cls.update_layout(
        title=dict(text=f"{sel_model} — Per-Class IoU Across 32 Semantic Classes (PalmCity RGB Palette)", font=dict(size=14, color="#0B2545")),
        font=dict(color="#000000"),
        xaxis=dict(
            range=[0, 1.08],
            title=dict(text="Class IoU", font=dict(color="#000000")),
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
        height=720,
        margin=dict(l=10, r=40, t=45, b=30),
    )
    st.plotly_chart(fig_cls, use_container_width=True)

    # Strategic Takeaway — PalmCity as Auxiliary Ground-Truth Layer for EO
    st.markdown(
        """
        <div class="eo-takeaway">
            🌍 <strong>Auxiliary Ground-Truth Value for Remote Sensing &amp; EO:</strong>
            While 360° street-level imagery is not orbital Earth Observation itself, within the broader <strong>Remote Sensing &amp; Deep Learning Computer Vision</strong> ecosystem it serves as a high-value <strong>auxiliary layer</strong> that anchors satellite analytics in local ground reality. Achieving near-ceiling accuracy on core structural classes (<strong>Sky: 0.99, Road: 0.94, Building: 0.93, Car: 0.87, Water: 0.87, Tree: 0.83</strong>) enables automated urban micro-environment indices (<em>GVI, SVF, Canyon Ratio</em>) and street-level validation that directly strengthen satellite-based urban monitoring and digital twins.
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# TAB 3: MULTI-BAND SAR WHEAT HEIGHT ESTIMATION (C-BAND & X-BAND)
# =========================================================
def render_crop_height():
    # 1. Business & Agricultural EO Context Banner
    st.markdown(
        """
        <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-left:5px solid #0D9488; border-radius:8px; padding:0.9rem 1.2rem; margin-bottom:1.2rem; font-size:0.95rem; color:#0F172A;">
            🌾 <strong>Why Wheat Height Matters for Agricultural EO Services:</strong>
            Canopy height is a primary biophysical indicator of <strong>crop vigor, biomass accumulation, lodging risk, and final grain yield</strong>.
            Because optical satellites are frequently blocked by spring cloud cover during key growth stages, <strong>Synthetic Aperture Radar (SAR)</strong> provides reliable, all-weather monitoring—enabling continuous, subscription-grade agricultural intelligence.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Auto-load metrics CSV if available
    sar_metrics_path = os.path.join(BASE_DIR, "latest_model_metrics.csv")
    df_sar_metrics = pd.read_csv(sar_metrics_path) if os.path.exists(sar_metrics_path) else None

    if df_sar_metrics is not None and not df_sar_metrics.empty:
        r2_col = next((c for c in df_sar_metrics.columns if "test_r2" in c.lower()), None)
        rmse_col = next((c for c in df_sar_metrics.columns if "test_rmse" in c.lower()), None)
        ablation_col = next((c for c in df_sar_metrics.columns if "ablation" in c.lower()), None)
        model_col = next((c for c in df_sar_metrics.columns if "model_name" in c.lower()), None)
        fs_col = next((c for c in df_sar_metrics.columns if "feature_selection" in c.lower()), None)

        best_row = df_sar_metrics.loc[df_sar_metrics[r2_col].idxmax()] if r2_col else df_sar_metrics.iloc[0]
        kpi_total_models = f"{len(df_sar_metrics)}"
        kpi_r2_val = f"{best_row[r2_col]:.3f}" if r2_col and pd.notna(best_row[r2_col]) else "—"
        kpi_rmse_val = f"{best_row[rmse_col]:.2f} cm" if rmse_col and pd.notna(best_row[rmse_col]) else "—"
        best_label = f"{best_row.get(model_col, 'Best')} • {best_row.get(ablation_col, 'SAR')} ({best_row.get(fs_col, 'FS')})"
    else:
        r2_col = rmse_col = ablation_col = model_col = fs_col = None
        kpi_total_models = "36"
        kpi_r2_val = "C + X Band"
        kpi_rmse_val = "All-Weather"
        best_label = "RF • XGBoost • LightGBM"

    # 2. Executive KPI Cards (Experiment Scale + Lightweight Efficiency + Accuracy)
    w1, w2, w3, w4 = st.columns(4)
    with w1:
        st.markdown(
            f"""
            <div class="kpi-card navy">
                <div class="kpi-label">🧪 Models Evaluated</div>
                <div class="kpi-value">{kpi_total_models} <span style="font-size:0.95rem; color:#64748B;">runs</span></div>
                <div class="kpi-sub">3 sensor setups × 3 algorithms × 4 feature sets</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with w2:
        st.markdown(
            """
            <div class="kpi-card amber">
                <div class="kpi-label">⚡ Feature Reduction</div>
                <div class="kpi-value">Up to 87%</div>
                <div class="kpi-sub">39 features pruned down to <strong>5–14</strong> key predictors</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with w3:
        st.markdown(
            f"""
            <div class="kpi-card success">
                <div class="kpi-label">🏆 Top Held-Out R²</div>
                <div class="kpi-value">{kpi_r2_val}</div>
                <div class="kpi-sub"><strong>{best_label}</strong></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with w4:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">📏 Held-Out Error (RMSE)</div>
                <div class="kpi-value">{kpi_rmse_val}</div>
                <div class="kpi-sub">Evaluated once on unseen 30% test fields</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # -----------------------------------------------------
    # SECTION 3.1: FIELD CAMPAIGN & STUDY AREA
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">GROUND TRUTH • IN-SITU AGRONOMIC CAMPAIGN</span>
            <h2>🌾 Study Area, Sampling Coordinates &amp; Multi-Date Field Visits</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    wf_col1, wf_col2 = st.columns(2, gap="medium")
    with wf_col1:
        img_w1 = load_image("wheat1_studyarea_samples.png")
        if img_w1 is not None:
            st.image(
                img_w1,
                caption="🗺️ Study Area & Geo-Referenced Wheat Height Sampling Coordinates",
                use_container_width=True,
            )
        else:
            st.info("Image `wheat1_studyarea_samples.png` not found in workspace.")
    with wf_col2:
        img_w2 = load_image("wheat1_fieldvisitphotos.png")
        if img_w2 is not None:
            st.image(
                img_w2,
                caption="📸 Multi-Date Field Visits Capturing Phenological Growth Stages",
                use_container_width=True,
            )
        else:
            st.info("Image `wheat1_fieldvisitphotos.png` not found in workspace.")

    st.markdown("---")

    # -----------------------------------------------------
    # SECTION 3.2: WHY BAND ABLATIONS & LIGHTWEIGHT FEATURE SELECTION?
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">SENSOR STRATEGY &amp; MODEL LIGHTWEIGHTING</span>
            <h2>📡 Satellite Band Ablations &amp; Plain-Language Feature Selection</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    exp_c1, exp_c2 = st.columns(2, gap="large")
    with exp_c1:
        st.markdown("**🛰️ Why Test C-Band, X-Band &amp; Combined Ablations?**")
        df_design = pd.DataFrame(
            [
                ("Only C-Band (23 → 3–8)", "Sentinel-1 (free & open). Penetrates deeper into the wheat canopy to capture stem and volume growth.", "Low-cost, scalable regional service"),
                ("Only X-Band (16 → 3–10)", "PAZ & TerraSAR-X (commercial VHR). Sensitive to upper-canopy structure, wheat heads, and surface roughness.", "High-precision parcel monitoring"),
                ("Combined C + X (39 → 5–14)", "Fuses both wavelengths to capture full vertical crop structure across early-to-late growth stages.", "Maximum accuracy & robustness"),
            ],
            columns=["Sensor Setup (Features)", "Physical Role in Wheat Monitoring", "Service Trade-Off"],
        )
        st.dataframe(df_design, use_container_width=True, hide_index=True, height=195)

    with exp_c2:
        st.markdown("**🎯 How We Make Models Lighter &amp; Faster (No-Code Overview)**")
        df_fs = pd.DataFrame(
            [
                ("ALL (Baseline)", "Uses every available radar feature without filtering."),
                ("LASSO", "Automatically drops redundant radar bands, keeping only the strongest linear contributors (down to 5 features)."),
                ("Mutual Information (MI)", "Ranks features by how strongly they track wheat height—even for non-linear growth curves."),
                ("SHAP-RFE", "Iteratively removes the least impactful features based on explainable AI importance until only the core drivers remain."),
            ],
            columns=["Strategy", "What It Does in Practice"],
        )
        st.dataframe(df_fs, use_container_width=True, hide_index=True, height=195)

    st.markdown(
        """
        <div class="insight-box">
            🌱 <strong>Physical Link Between Selected Radar Features &amp; Wheat Growth:</strong>
            Across all 27 feature-selection runs, the models consistently converged on a compact set of physically meaningful predictors:
            <strong>IDPDD</strong> (consistently selected across Sentinel-1, PAZ &amp; TDX—tracking structural depolarization as stems elongate),
            <strong>VH / VV backscatter &amp; ratios</strong> (sensitive to canopy water content and biomass density),
            <strong>RVI</strong> (Radar Vegetation Index), and <strong>X-band coherence (coh_HH / coh_VV)</strong> (capturing canopy stability and structural change between passes).
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("📋 View Complete Selected Features Table (All 27 Sensor × Model × Strategy Runs)"):
        df_sel_feats = pd.DataFrame(
            [
                ("Only C-Band (23)", "RF", "LASSO", 8, "S1A87_IDPDD, S1A87_VH, S1A87_VV, S1A160_Ratio, S1D65_IDPDD, S1D65_VH, S1D167_VH, S1D167_VV"),
                ("Only C-Band (23)", "RF", "MI", 3, "S1A87_IDPDD, S1D65_IDPDD, S1D167_IDPDD"),
                ("Only C-Band (23)", "RF", "SHAP-RFE", 6, "S1A87_VH, S1D65_IDPDD, S1D65_VH, S1D65_VV, S1D167_IDPDD, S1D167_VV"),
                ("Only C-Band (23)", "XGBoost", "LASSO", 8, "S1A87_IDPDD, S1A87_VH, S1A87_VV, S1A160_Ratio, S1D65_IDPDD, S1D65_VH, S1D167_VH, S1D167_VV"),
                ("Only C-Band (23)", "XGBoost", "MI", 8, "S1A87_IDPDD, S1A87_VH, S1A87_VV, S1D65_IDPDD, S1D65_VH, S1D167_IDPDD, S1D167_VH, S1D167_VV"),
                ("Only C-Band (23)", "XGBoost", "SHAP-RFE", 6, "S1A87_VH, S1D65_IDPDD, S1D65_VH, S1D65_VV, S1D167_IDPDD, S1D167_VV"),
                ("Only C-Band (23)", "LightGBM", "LASSO", 8, "S1A87_IDPDD, S1A87_VH, S1A87_VV, S1A160_Ratio, S1D65_IDPDD, S1D65_VH, S1D167_VH, S1D167_VV"),
                ("Only C-Band (23)", "LightGBM", "MI", 8, "S1A87_IDPDD, S1A87_VH, S1A87_VV, S1D65_IDPDD, S1D65_VH, S1D167_IDPDD, S1D167_VH, S1D167_VV"),
                ("Only C-Band (23)", "LightGBM", "SHAP-RFE", 6, "S1A87_VH, S1D65_IDPDD, S1D65_VH, S1D65_VV, S1D167_IDPDD, S1D167_VV"),
                ("Only X-Band (16)", "RF", "LASSO", 6, "PAZ_IDPDD, PAZ_RVI, PAZ_VV, TDX_HH, TDX_IDPDD, TDX_RVI"),
                ("Only X-Band (16)", "RF", "MI", 3, "PAZ_IDPDD, TDX_IDPDD, TDX_VV"),
                ("Only X-Band (16)", "RF", "SHAP-RFE", 3, "PAZ_IDPDD, TDX_IDPDD, TDX_VV"),
                ("Only X-Band (16)", "XGBoost", "LASSO", 8, "PAZ_IDPDD, PAZ_RVI, PAZ_VV, coh_HH_35, coh_HH_48, TDX_HH, TDX_IDPDD, TDX_VDDPI"),
                ("Only X-Band (16)", "XGBoost", "MI", 10, "PAZ_IDPDD, PAZ_RVI, PAZ_VV, coh_HH_35, coh_VV_35, coh_HH_48, coh_VV_48, TDX_IDPDD, TDX_VDDPI, TDX_VV"),
                ("Only X-Band (16)", "XGBoost", "SHAP-RFE", 5, "PAZ_IDPDD, PAZ_VV, coh_VV_35, TDX_IDPDD, TDX_VV"),
                ("Only X-Band (16)", "LightGBM", "LASSO", 6, "PAZ_IDPDD, PAZ_RVI, PAZ_VV, TDX_HH, TDX_IDPDD, TDX_RVI"),
                ("Only X-Band (16)", "LightGBM", "MI", 5, "PAZ_IDPDD, PAZ_VV, TDX_HH, TDX_IDPDD, TDX_VV"),
                ("Only X-Band (16)", "LightGBM", "SHAP-RFE", 8, "PAZ_IDPDD, PAZ_Ratio, PAZ_VV, coh_HH_35, coh_VV_35, TDX_HH, TDX_IDPDD, TDX_VV"),
                ("Combined (39)", "RF", "LASSO", 5, "PAZ_IDPDD, S1A160_VV, S1D65_IDPDD, S1D65_VH, TDX_IDPDD"),
                ("Combined (39)", "RF", "MI", 10, "PAZ_IDPDD, S1A87_IDPDD, S1A87_VH, S1A87_VV, S1D65_IDPDD, S1D65_VH, S1D65_VV, S1D167_IDPDD, S1D167_VV, TDX_VV"),
                ("Combined (39)", "RF", "SHAP-RFE", 14, "PAZ_HH, PAZ_IDPDD, PAZ_Ratio, coh_HH_35, coh_VV_35, S1A87_IDPDD, S1A87_VH, S1A87_VV, S1A160_RVI, S1D65_IDPDD, S1D65_Ratio, S1D167_IDPDD, S1D167_VV, TDX_VDDPI"),
                ("Combined (39)", "XGBoost", "LASSO", 5, "PAZ_IDPDD, S1A160_VV, S1D65_IDPDD, S1D65_VH, TDX_IDPDD"),
                ("Combined (39)", "XGBoost", "MI", 8, "PAZ_IDPDD, S1A87_IDPDD, S1A87_VH, S1D65_IDPDD, S1D65_VH, S1D167_IDPDD, S1D167_VV, TDX_VV"),
                ("Combined (39)", "XGBoost", "SHAP-RFE", 9, "PAZ_IDPDD, S1A87_IDPDD, S1D65_IDPDD, S1D65_VH, S1D65_VV, S1D167_IDPDD, S1D167_VV, TDX_Ratio, TDX_VV"),
                ("Combined (39)", "LightGBM", "LASSO", 5, "PAZ_IDPDD, S1A160_VV, S1D65_IDPDD, S1D65_VH, TDX_IDPDD"),
                ("Combined (39)", "LightGBM", "MI", 10, "PAZ_IDPDD, S1A87_IDPDD, S1A87_VH, S1A87_VV, S1D65_IDPDD, S1D65_VH, S1D65_VV, S1D167_IDPDD, S1D167_VV, TDX_VV"),
                ("Combined (39)", "LightGBM", "SHAP-RFE", 9, "PAZ_IDPDD, S1A87_IDPDD, S1D65_IDPDD, S1D65_VH, S1D65_VV, S1D167_IDPDD, S1D167_VV, TDX_Ratio, TDX_VV"),
            ],
            columns=["Sensor Setup", "Model", "Feature Selection", "# Selected", "Selected Features"],
        )
        st.dataframe(df_sel_feats, use_container_width=True, hide_index=True, height=340)

    st.markdown("---")

    # -----------------------------------------------------
    # SECTION 3.3: CLEAN R² BENCHMARK (HIGHLIGHTING STRONGEST ABLATION & MODELS)
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">MODEL PERFORMANCE • HELD-OUT TEST R²</span>
            <h2>📊 Ablation × Model × Feature Selection Benchmark (R²)</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if df_sar_metrics is not None and not df_sar_metrics.empty and r2_col is not None:
        df_r2 = df_sar_metrics.dropna(subset=[r2_col]).copy()
        if model_col and fs_col and ablation_col:
            df_r2["Label"] = (
                df_r2[ablation_col].astype(str)
                + " | "
                + df_r2[model_col].astype(str)
                + " ("
                + df_r2[fs_col].astype(str)
                + ")"
            )
        else:
            df_r2["Label"] = df_r2.index.astype(str)

        # Keep top 12 configurations sorted by R² so the chart stays crisp & projection-ready
        df_top_r2 = df_r2.sort_values(r2_col, ascending=False).head(12).sort_values(r2_col, ascending=True)

        fig_sar = px.bar(
            df_top_r2,
            y="Label",
            x=r2_col,
            color=ablation_col if ablation_col else None,
            orientation="h",
            text=df_top_r2[r2_col].map(lambda v: f"{v:.3f}"),
            color_discrete_sequence=["#0D9488", "#0077B6", "#D97706"],
            title="Top 12 Configurations by Held-Out Test R² (Strongest Sensor Ablation & Lightweight Models)",
        )
        fig_sar.update_traces(
            textposition="outside",
            textfont=dict(color="#000000", size=13),
            cliponaxis=False,
        )
        max_r2 = float(df_top_r2[r2_col].max())
        min_r2 = max(0.0, float(df_top_r2[r2_col].min()) - 0.08)
        fig_sar.update_layout(
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            font=dict(color="#000000", size=13),
            height=480,
            margin=dict(l=15, r=65, t=65, b=40),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="left",
                x=0,
                title="",
                font=dict(color="#000000", size=12),
            ),
            xaxis=dict(
                range=[min_r2, min(1.05, max_r2 + 0.08)],
                title=dict(text="Held-Out Test R²", font=dict(color="#000000", size=13)),
                tickfont=dict(color="#000000", size=12),
                showgrid=True,
                gridcolor="#E2E8F0",
            ),
            yaxis=dict(
                title=dict(text="", font=dict(color="#000000")),
                tickfont=dict(color="#000000", size=12),
                automargin=True,
            ),
            title_font=dict(size=15, color="#0B2545"),
        )
        st.plotly_chart(fig_sar, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info(
            "📂 Place `latest_model_metrics.csv` into `/workspaces/30Nov2026_Planetek/` to render the Top-12 Held-Out R² bar chart automatically."
        )

    # 3. Planetek-Aligned Operational Takeaway
    st.markdown(
        """
        <div class="eo-takeaway">
            🚀 <strong>Operational EO Strategy — Lightweight Pipelines for Planetek Agricultural Services:</strong>
            By pruning 39 radar indicators down to <strong>5–14 physically grounded features</strong> (such as <em>IDPDD</em> and dual-pol backscatter), this workflow delivers <strong>faster, lighter, and more generalizable</strong> crop-monitoring models without sacrificing accuracy. Comparing free <strong>Sentinel-1 (C-band)</strong> against commercial <strong>PAZ/TDX (X-band)</strong> directly supports tiered, cloud-ready EO service design—aligned with Planetek's continuous monitoring platforms (e.g., <em>Rheticus</em>) for scalable, all-weather agronomy.
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# TAB 4: FOUNDATION MODELS & ALPHAEARTH FOR POLSAR CROP MONITORING
# =========================================================
def render_foundation():
    # Context Banner
    st.markdown(
        """
        <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:0.75rem 1.1rem; margin-bottom:1.2rem; font-size:0.92rem; color:#334155;">
            🌾 <strong>Project Overview:</strong> <em>Foundation Models for Crop Monitoring with Sparse Full-Polarimetric RADARSAT-2 Data</em> —
            a spatially-separated, tile-based rice segmentation benchmark across two Mediterranean/Balkan agricultural sites:
            <strong>Saedinenie (Bulgaria)</strong> and <strong>Gönen (Türkiye)</strong>.
            We systematically benchmark <strong>Vision Foundation Models (SAM ViT-B, DINOv2-B)</strong>, <strong>Classic Deep Nets (SegFormer-B3, DeepLabV3+)</strong>, and <strong>Pixel-Based ML (XGBoost, RF, LightGBM, LogReg)</strong> across single-date PolSAR features vs. <strong>AlphaEarth Foundations embeddings</strong>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # KPI Cards — Tab 4
    r1, r2, r3, r4 = st.columns(4)
    with r1:
        st.markdown(
            """
            <div class="kpi-card success">
                <div class="kpi-label">🥇 Overall Leader (AlphaEarth)</div>
                <div class="kpi-value">94.83% <span style="font-size:0.95rem; color:#64748B;">mIoU</span></div>
                <div class="kpi-sub"><strong>XGBoost • AlphaEarth-64</strong> (Rice IoU: 92.37% • κ: 0.95)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with r2:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">📡 Best SAR-Only Model</div>
                <div class="kpi-value">90.64% <span style="font-size:0.95rem; color:#64748B;">mIoU</span></div>
                <div class="kpi-sub"><strong>SAM ViT-B • Freeman</strong> (Rice IoU: 86.24% • OA: 96.22%)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with r3:
        st.markdown(
            """
            <div class="kpi-card navy">
                <div class="kpi-label">🗺️ Validation Benchmark</div>
                <div class="kpi-value">392,081 <span style="font-size:0.95rem; color:#64748B;">px</span></div>
                <div class="kpi-sub">Saedinenie: 299.9K • Gönen: 92.2K (25.34% Rice)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with r4:
        st.markdown(
            """
            <div class="kpi-card amber">
                <div class="kpi-label">⚡ Linear Separability</div>
                <div class="kpi-value">94.18% <span style="font-size:0.95rem; color:#64748B;">mIoU</span></div>
                <div class="kpi-sub">Even <strong>Logistic Regression</strong> excels on AlphaEarth-64</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # -----------------------------------------------------
    # SECTION 4.1: INPUT FEATURE SETS & STUDY SITES
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">STUDY SITES &amp; MULTI-MODAL INPUTS</span>
            <h2>🛰️ Single-Date PolSAR Features vs. AlphaEarth Embeddings (Saedinenie &amp; Gönen)</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "Backscatter and polarimetric decompositions (**Freeman** & **H/A/α**) delineate rice parcels clearly, whereas **GLCM texture** blurs parcel boundaries. "
        "By contrast, **AlphaEarth (PCA-3)** appears smooth and almost cartographic—reflecting its nature as an annual, multi-source geospatial embedding rather than a single-date radar snapshot."
    )

    site_c1, site_c2 = st.columns(2, gap="medium")
    with site_c1:
        img_bg = load_image("pirinc_bulgaristan.png")
        if img_bg is not None:
            st.image(
                img_bg,
                caption="🇧🇬 Saedinenie Site (a–g): (a) SAR intensity; (b) backscatter; (c) Freeman; (d) H/A/α; (e) GLCM; (f) AlphaEarth PCA-3; (g) reference data.",
                use_container_width=True,
            )
        else:
            st.info("Image `pirinc_bulgaristan.png` not found in workspace.")
    with site_c2:
        img_tr = load_image("pirinc_turkiye.png")
        if img_tr is not None:
            st.image(
                img_tr,
                caption="🇹🇷 Gönen Site (h–n): (h) SAR intensity; (i) backscatter; (j) Freeman; (k) H/A/α; (l) GLCM; (m) AlphaEarth PCA-3; (n) reference data.",
                use_container_width=True,
            )
        else:
            st.info("Image `pirinc_turkiye.png` not found in workspace.")

    st.markdown("---")

    # -----------------------------------------------------
    # SECTION 4.2: BENCHMARK RANKING & CLASSIFIER × INPUT MATRIX
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">QUANTITATIVE BENCHMARK • 42 CONFIGURATIONS</span>
            <h2>📊 Foundation Models vs. Classic Deep Nets vs. Pixel-Based ML</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    radarsat_top_data = [
        (1, "XGBoost (pixel)", "AlphaEarth (64 bands)", "AlphaEarth", 94.83, 92.37, 97.95, 0.95, 99.99, 91.34),
        (2, "Random Forest (pixel)", "AlphaEarth (64 bands)", "AlphaEarth", 94.64, 92.08, 97.88, 0.94, 99.99, 91.02),
        (3, "LightGBM (pixel)", "AlphaEarth (64 bands)", "AlphaEarth", 94.55, 91.95, 97.85, 0.94, 99.99, 90.88),
        (4, "SAM ViT-B (FM)", "AlphaEarth (PCA-3)", "AlphaEarth", 93.80, 90.92, 97.51, 0.94, 99.52, 90.97),
        (5, "DINOv2-B (FM)", "AlphaEarth (PCA-3)", "AlphaEarth", 93.74, 90.77, 97.51, 0.93, 99.82, 89.99),
        (6, "DeepLabV3+ (R50)", "AlphaEarth (PCA-3)", "AlphaEarth", 91.85, 88.17, 96.64, 0.91, 98.03, 92.12),
        (7, "SegFormer-B3", "AlphaEarth (PCA-3)", "AlphaEarth", 90.92, 86.88, 96.22, 0.90, 97.70, 91.39),
        (8, "SAM ViT-B (FM)", "Freeman decomposition", "SAR Deep / FM", 90.64, 86.24, 96.22, 0.90, 98.36, 89.24),
        (9, "SAM ViT-B (FM)", "H/A/α decomposition", "SAR Deep / FM", 90.14, 85.41, 96.06, 0.90, 97.32, 91.94),
        (10, "SAM ViT-B (FM)", "SAR-all (stacked)", "SAR Deep / FM", 89.96, 85.31, 95.90, 0.89, 97.98, 89.13),
        (11, "SegFormer-B3", "Backscatter", "SAR Deep / FM", 88.49, 83.15, 95.26, 0.88, 96.98, 89.68),
        (12, "DeepLabV3+ (R50)", "Backscatter", "SAR Deep / FM", 88.07, 82.62, 95.05, 0.87, 97.87, 85.86),
        (13, "DINOv2-B (FM)", "Freeman decomposition", "SAR Deep / FM", 88.04, 82.42, 95.10, 0.87, 98.06, 85.50),
        (24, "Random Forest (pixel)", "SAR-all (stacked)", "SAR Pixel ML", 76.58, 67.18, 89.10, 0.73, 92.49, 78.10),
        (27, "Random Forest (pixel)", "Backscatter", "SAR Pixel ML", 73.09, 62.49, 87.17, 0.68, 91.65, 72.60),
        (30, "SAM ViT-B (FM)", "GLCM texture", "SAR Deep / FM", 70.86, 58.07, 86.67, 0.65, 85.87, 89.29),
        (40, "XGBoost (pixel)", "GLCM texture", "SAR Pixel ML", 44.54, 31.56, 64.47, 0.24, 60.63, 76.96),
    ]
    df_rs = pd.DataFrame(
        radarsat_top_data,
        columns=[
            "Rank", "Classifier", "Input", "Group", "mIoU (%)",
            "Rice IoU (%)", "OA (%)", "Kappa", "Saedinenie OA (%)", "Gönen OA (%)",
        ],
    )
    df_rs["Label"] = df_rs["Classifier"] + " • " + df_rs["Input"]

    rs_col1, rs_col2 = st.columns([1.2, 1], gap="large")
    with rs_col1:
        metric_sel = st.radio(
            "Select Metric to Compare Key Configurations:",
            ["mIoU (%)", "Rice IoU (%)"],
            horizontal=True,
        )
        df_rs_plot = df_rs.sort_values(metric_sel, ascending=True)
        grp_colors = {
            "AlphaEarth": "#0D9488",
            "SAR Deep / FM": "#0077B6",
            "SAR Pixel ML": "#D97706",
        }
        fig_rs = px.bar(
            df_rs_plot,
            y="Label",
            x=metric_sel,
            color="Group",
            orientation="h",
            text=df_rs_plot[metric_sel].map(lambda v: f"{v:.2f}%"),
            color_discrete_map=grp_colors,
            title=f"Pooled Validation {metric_sel} — AlphaEarth vs. SAR Deep/FM vs. Pixel ML",
        )
        fig_rs.update_traces(textposition="outside", textfont=dict(color="#000000", size=10))
        fig_rs.update_layout(
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            font=dict(color="#000000"),
            height=480,
            margin=dict(l=10, r=45, t=45, b=30),
            legend=dict(orientation="h", yanchor="bottom", y=1.01, xanchor="right", x=1, title="", font=dict(color="#000000")),
            xaxis=dict(
                range=[25, 104],
                title=dict(text=metric_sel, font=dict(color="#000000")),
                tickfont=dict(color="#000000"),
                showgrid=True,
                gridcolor="#F1F5F9",
            ),
            yaxis=dict(
                title=dict(text="Configuration", font=dict(color="#000000")),
                tickfont=dict(color="#000000"),
            ),
            title_font=dict(size=13.5, color="#0B2545"),
        )
        st.plotly_chart(fig_rs, use_container_width=True)

    with rs_col2:
        st.markdown("**📋 Highlighted Configurations &amp; Per-Site OA (%)**")

        show_cols = ["Rank", "Classifier", "Input", "mIoU (%)", "Rice IoU (%)", "Saedinenie OA (%)", "Gönen OA (%)"]

        def highlight_ae(row):
            grp = df_rs.loc[row.name, "Group"]
            if grp == "AlphaEarth":
                return ["background-color: #CCFBF1; color: #0B2545"] * len(row)
            if row["Rank"] == 8:
                return ["background-color: #E0F2FE; font-weight: 700; color: #0B2545"] * len(row)
            return [""] * len(row)

        st.dataframe(
            df_rs[show_cols].style.apply(highlight_ae, axis=1).format(
                {"mIoU (%)": "{:.2f}", "Rice IoU (%)": "{:.2f}", "Saedinenie OA (%)": "{:.2f}", "Gönen OA (%)": "{:.2f}"}
            ),
            use_container_width=True,
            hide_index=True,
            height=420,
        )

    # Matrix & Confusion Matrices Side-by-Side
    st.markdown("**🖼️ Classifier × Input Matrix &amp; Pooled Confusion Matrices**")
    mat_c1, mat_c2 = st.columns(2, gap="medium")
    with mat_c1:
        img_miou = load_image("pirinc_mIoU.png")
        if img_miou is not None:
            st.image(
                img_miou,
                caption="📊 Classifier × input matrix of (a) mIoU and (b) rice IoU (%) on validation tiles (both sites pooled). † AlphaEarth used 64 bands for pixel classifiers and PCA-3 for deep models.",
                use_container_width=True,
            )
        else:
            st.info("Image `pirinc_mIoU.png` not found in workspace.")
    with mat_c2:
        img_cm = load_image("pirinc_confmatrixes.png")
        if img_cm is not None:
            st.image(
                img_cm,
                caption="🧩 Confusion matrices (validation tiles, both sites pooled) of the best configuration per input set: (a) AlphaEarth-64, (b) Freeman, (c) H/A/α, (d) backscatter, (e) GLCM, (f) SAR-all.",
                use_container_width=True,
            )
        else:
            st.info("Image `pirinc_confmatrixes.png` not found in workspace.")

    st.markdown("---")

    # -----------------------------------------------------
    # SECTION 4.3: PREDICTED & ERROR MAPS (SAEDINENIE & GÖNEN)
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">PARCEL-LEVEL SPATIAL DIAGNOSTICS</span>
            <h2>🗺️ Predicted Maps &amp; Error Maps Across Both Agricultural Sites</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    err_c1, err_c2 = st.columns(2, gap="medium")
    with err_c1:
        img_ebg = load_image("pirinc_predict_error_bulgaristan.png")
        if img_ebg is not None:
            st.image(
                img_ebg,
                caption="🇧🇬 Saedinenie Site: (a) reference data, (b–g) predicted maps, and (h–m) error maps of the best configuration for each input set.",
                use_container_width=True,
            )
        else:
            st.info("Image `pirinc_predict_error_bulgaristan.png` not found in workspace.")
    with err_c2:
        img_etr = load_image("pirinc_predict_error_turkiye.png")
        if img_etr is not None:
            st.image(
                img_etr,
                caption="🇹🇷 Gönen Site: (a) reference data, (b–g) predicted maps, and (h–m) error maps of the best configuration for each input set.",
                use_container_width=True,
            )
        else:
            st.info("Image `pirinc_predict_error_turkiye.png` not found in workspace.")

    # Key Insights
    st.markdown(
        """
        <div class="insight-box">
            🔍 <strong>Spatial Context vs. Speckle Noise:</strong>
            On identical single-date SAR inputs, deep segmentation models outperform pixel-based ML by <strong>+15 to +25 mIoU points</strong> (e.g., Backscatter: 87.6–88.5% vs. 72.9–73.1%). Learning whole-parcel geometry suppresses SAR speckle and eliminates the salt-and-pepper commission errors visible in Random Forest maps.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Bridge Takeaway to Tab 5 (AlphaEarth & Embeddings)
    st.markdown(
        """
        <div class="eo-takeaway">
            🌍 <strong>Bridge to Next Module — Why AlphaEarth &amp; Geospatial Embeddings Change the Game:</strong>
            All top positions in this benchmark are dominated by <strong>AlphaEarth Foundations embeddings</strong> (up to <strong>94.83% mIoU</strong>, <strong>99.99% OA</strong> at Saedinenie). Remarkably, even a simple linear classifier (Logistic Regression: <strong>94.18% mIoU</strong>) matches heavy vision transformers once data are projected into AlphaEarth's 64-D annual multi-source embedding space—proving that <strong>universal EO representations</strong> drastically lower compute, labeling, and sensor-fusion barriers. ➡️ <em>Explore AlphaEarth Foundations in detail in Tab 5.</em>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# TAB 5: ALPHAEARTH FOUNDATIONS & GEOSPATIAL EMBEDDINGS
# =========================================================
def render_alphaearth():
    # Context Banner
    st.markdown(
        """
        <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:0.75rem 1.1rem; margin-bottom:1.2rem; font-size:0.92rem; color:#334155;">
            🌐 <strong>Next-Generation EO Paradigm — AlphaEarth Foundations (Google DeepMind):</strong>
            Moving beyond manual feature engineering and single-date snapshots, AlphaEarth acts as a <em>"virtual satellite"</em>—compressing multi-sensor, multi-temporal Earth observation sequences into a standardized, ready-to-use <strong>64-dimensional unit-normalized embedding field</strong> at <strong>10 m</strong> resolution for every land pixel and year.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 3-Concept Taxonomy Strip (Dataset vs Foundation Model vs Embedding Dataset)
    t_c1, t_c2, t_c3 = st.columns(3, gap="medium")
    with t_c1:
        st.markdown(
            """
            <div class="kpi-card navy">
                <div class="kpi-label">1️⃣ EO Dataset</div>
                <div class="kpi-value" style="font-size:1.25rem;">Raw Observations</div>
                <div class="kpi-sub">Multi-sensor archives (Sentinel-1/2, Landsat, GEDI, ERA5) used to train models.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with t_c2:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">2️⃣ Foundation Model</div>
                <div class="kpi-value" style="font-size:1.25rem;">AlphaEarth (STP)</div>
                <div class="kpi-sub">Pretrained spatiotemporal neural encoder transferable across diverse mapping tasks.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with t_c3:
        st.markdown(
            """
            <div class="kpi-card success">
                <div class="kpi-label">3️⃣ Embedding Dataset</div>
                <div class="kpi-value" style="font-size:1.25rem;">Satellite Embedding V1</div>
                <div class="kpi-sub">Precomputed 64-D vectors (<code>A00–A63</code>) usable directly without re-running inference.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # KPI Cards — Technical Specs
    ae1, ae2, ae3, ae4 = st.columns(4)
    with ae1:
        st.markdown(
            """
            <div class="kpi-card success">
                <div class="kpi-label">📐 Embedding Space</div>
                <div class="kpi-value">64-D <span style="font-size:0.95rem; color:#64748B;">on S⁶³</span></div>
                <div class="kpi-sub">Bands <code>A00–A63</code> • Unit-normalized (‖z‖₂ ≈ 1)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with ae2:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">🛰️ Spatial Grid</div>
                <div class="kpi-value">10 m</div>
                <div class="kpi-sub">Global terrestrial surfaces &amp; shallow waters</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with ae3:
        st.markdown(
            """
            <div class="kpi-card navy">
                <div class="kpi-label">📅 Temporal Product</div>
                <div class="kpi-value">Annual</div>
                <div class="kpi-sub">2017–2024 (GEE) &amp; 2025 (GCS COGs)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with ae4:
        st.markdown(
            """
            <div class="kpi-card amber">
                <div class="kpi-label">☁️ Cloud Access</div>
                <div class="kpi-value">GEE / GCS</div>
                <div class="kpi-sub"><code>GOOGLE/SATELLITE_EMBEDDING/V1/ANNUAL</code></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # -----------------------------------------------------
    # SECTION 5.1: CORE MECHANICS & VISUAL ARCHITECTURE
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">REPRESENTATION LEARNING • 64 NUMBERS FOR EVERY PIXEL</span>
            <h2>🧠 How AlphaEarth Works: Space-Time-Precision (STP) &amp; Teacher–Student Consistency</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="pipeline-strip">
            <strong>⚡ Spatiotemporal Representation Pipeline:</strong> &nbsp;
            🛰️ Irregular Multi-Sensor Sequences (Optical, SAR, LiDAR, Climate, Text) &nbsp;➡️&nbsp;
            🧭 <strong>Space-Time-Precision (STP) Encoder</strong> &nbsp;➡️&nbsp;
            🤝 <strong>Teacher–Student Consistency</strong> &nbsp;➡️&nbsp;
            🌐 <strong>64-D Unit Vector</strong> <code>z<sub>p,t</sub> = [A00, …, A63]</code>
        </div>
        """,
        unsafe_allow_html=True,
    )

    ae_img_c1, ae_img_c2 = st.columns(2, gap="medium")
    with ae_img_c1:
        img_ae1 = load_image("alphaearth_field.jpg")
        if img_ae1 is not None:
            st.image(
                img_ae1,
                caption="🌐 Global Embedding Field: Mapping any Earth pixel into 64 learned latent axes (A00–A63) normalized onto the unit hypersphere S⁶³.",
                use_container_width=True,
            )
        else:
            st.info("Save the Global Embedding Field graphic as `alphaearth_field.jpg` in `/workspaces/30Nov2026_Planetek/`.")
    with ae_img_c2:
        img_ae2 = load_image("alphaearth_gcs.jpg")
        if img_ae2 is not None:
            st.image(
                img_ae2,
                caption="☁️ Cloud-Native Delivery: Annual Cloud Optimized GeoTIFFs (COGs) on Google Cloud Storage (signed int8 quantized with de-quantization mapping).",
                use_container_width=True,
            )
        else:
            st.info("Save the GCS bucket graphic as `alphaearth_gcs.jpg` in `/workspaces/30Nov2026_Planetek/`.")

    st.write("")

    # -----------------------------------------------------
    # SECTION 5.2: INTERACTIVE TECHNICAL DEEP-DIVE
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">TECHNICAL DEEP-DIVE</span>
            <h2>🔍 Multimodal Inputs, PCA Comparison &amp; Critical Limitations</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    ae_view = st.radio(
        "Select Technical Perspective to Inspect:",
        [
            "🛰️ Multimodal Training Sources",
            "⚖️ PCA vs. AlphaEarth Embeddings",
            "⚠️ Scientific Limitations & Nuances",
        ],
        horizontal=True,
    )

    if "Multimodal" in ae_view:
        df_ae_sources = pd.DataFrame(
            [
                ("Sentinel-2", "Optical Multispectral", "Surface spectral observations"),
                ("Landsat 8/9", "Optical & Thermal", "Long-term surface & thermal observations"),
                ("Sentinel-1", "Radar / SAR", "All-weather surface structure & scattering"),
                ("PALSAR-2", "L-Band Radar", "Additional canopy & structural radar information"),
                ("GEDI", "LiDAR-Derived", "Vegetation height & vertical structure supervision"),
                ("GLO-30", "Elevation (DEM)", "Topographic & terrain context"),
                ("ERA5-Land", "Climate / Reanalysis", "Environmental & meteorological context"),
                ("GRACE", "Gravity / Geophysical", "Large-scale hydrological & geophysical context"),
                ("NLCD", "Land-Cover Labels", "Semantic training supervision"),
                ("Wikipedia / Geo-Text", "Geolocated Text", "Contrastive semantic supervision"),
            ],
            columns=["Data Source", "Modality / Type", "Role in AlphaEarth Framework"],
        )
        st.dataframe(df_ae_sources, use_container_width=True, hide_index=True, height=385)
        st.caption(
            "Note: Sources contribute via diverse spatial supports, temporal availabilities, and training objectives—not every source is a direct 10 m input at every pixel and year."
        )

    elif "PCA" in ae_view:
        df_pca_vs = pd.DataFrame(
            [
                ("Nature", "Statistical dimensionality reduction", "Neural representation learning"),
                ("Optimization", "Maximizes statistical variance in input data", "Teacher–student consistency & multimodal objectives"),
                ("Mapping", "Linear combinations of input bands", "Non-linear spatiotemporal latent features"),
                ("Scope", "Fitted locally to a single dataset", "Pretrained globally on large-scale EO archives"),
                ("Transferability", "No inherent semantic task awareness", "Designed for sparse-label downstream transfer"),
            ],
            columns=["Dimension", "Classical PCA", "AlphaEarth Foundations (64-D)"],
        )
        st.dataframe(df_pca_vs, use_container_width=True, hide_index=True, height=225)
        st.markdown(
            """
            <div class="insight-box">
                💡 <strong>Why 64 Dimensions?</strong> Latent dimensions (<code>A00–A63</code>) do <em>not</em> map 1-to-1 to physical variables (e.g., "A00 = NDVI"). Instead, they balance information capacity, storage efficiency, and downstream usability—allowing lightweight tabular models (<strong>XGBoost, RF, LightGBM, Logistic Regression</strong>) to achieve top-tier accuracy without retraining a Vision Transformer.
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:
        df_limits = pd.DataFrame(
            [
                ("Latent Interpretability", "Individual dimensions lack direct physical meaning; feature importance does not directly reveal physical mechanisms."),
                ("Grid vs. Effective Resolution", "A 10 m output grid does not guarantee that all encoded signals (e.g., climate or gravity) originate at 10 m precision."),
                ("Annual Cadence", "Summarizes an annual temporal context—not a continuous daily or monthly monitoring stream."),
                ("Temporal Comparability", "Year-to-year vector shifts can reflect observation availability or sensor artifacts, requiring ground validation."),
                ("Information Compression", "Subtle task-specific spectral/biochemical signatures may be lost compared to tailored physical indices."),
            ],
            columns=["Limitation", "Operational & Scientific Implication"],
        )
        st.dataframe(df_limits, use_container_width=True, hide_index=True, height=225)

    st.markdown("---")

    # -----------------------------------------------------
    # SECTION 5.3: INTERACTIVE STORAGE CALCULATOR & RESEARCH WORKFLOW
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="section-header">
            <span class="section-badge">OPERATIONAL SCALING &amp; SCIENTIFIC METHODOLOGY</span>
            <h2>⚙️ Cloud Footprint Estimator &amp; Recommended Hybrid EO Workflow</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    calc_c1, calc_c2 = st.columns([1, 1.25], gap="large")

    with calc_c1:
        st.markdown("**💾 10 m × 64-Band Storage Footprint Calculator**")
        area_km2 = st.slider(
            "Select Study Area Size (km²):",
            min_value=10,
            max_value=5000,
            value=100,
            step=10,
        )
        n_pixels = area_km2 * 10_000  # 1 km² = 10,000 pixels at 10 m
        raw_f32_mb = (n_pixels * 64 * 4) / 1e6
        quant_i8_mb = (n_pixels * 64 * 1) / 1e6

        st.markdown(
            f"""
            <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:0.9rem 1.1rem; font-size:0.9rem; color:#0F172A;">
                <div>📍 <strong>Pixels (10 m grid):</strong> {n_pixels:,}</div>
                <div style="margin-top:6px;">📦 <strong>Uncompressed Float32:</strong> <strong>{raw_f32_mb:,.1f} MB</strong> ({raw_f32_mb/1000:.2f} GB)</div>
                <div style="margin-top:6px;">🗜️ <strong>GCS Signed Int8 COG (~4× smaller):</strong> <strong>{quant_i8_mb:,.1f} MB</strong> ({quant_i8_mb/1000:.2f} GB)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("Illustrates why cloud-native access (GEE / GCS COGs) is essential for regional-to-national EO pipelines.")

    with calc_c2:
        st.markdown("**🔬 Rigorous Comparative EO Research Design (Model A vs. B vs. C)**")
        df_workflow = pd.DataFrame(
            [
                ("Model A — Conventional EO", "Spectral bands, indices (NDVI/NDWI), PolSAR & temporal stats", "Physical interpretability & baseline"),
                ("Model B — AlphaEarth Only", "64 learned embedding dimensions (A00–A63)", "Rapid sparse-label transfer & low compute"),
                ("Model C — Hybrid Fusion", "AlphaEarth embeddings + selected physical SAR/optical features", "Best of both worlds under spatial CV"),
            ],
            columns=["Strategy", "Feature Representation", "Scientific Value"],
        )
        st.dataframe(df_workflow, use_container_width=True, hide_index=True, height=160)

    # Final Vision & Fit Takeaway for Planetek Italia
    st.markdown(
        """
        <div class="eo-takeaway">
            🚀 <strong>Vision &amp; Fit for Planetek Italia (Bari, 2026):</strong>
            Across all five modules—from <strong>post-earthquake VHR damage mapping &amp; national building benchmarks</strong> (Tab 1), <strong>360° street-level urban analytics</strong> (Tab 2), and <strong>multi-band SAR crop-height regression</strong> (Tab 3), to <strong>PolSAR foundation-model benchmarks</strong> (Tab 4) and <strong>AlphaEarth geospatial embeddings</strong> (Tab 5)—this research focuses on turning heterogeneous, cloud-scale Earth Observation into <strong>leakage-free, explainable, and operational intelligence</strong>. Combining physical EO rigor with foundation-model embeddings directly supports scalable R&amp;D and next-generation EO services.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# 3. PERFORMANCE-AWARE NAVIGATION
# ---------------------------------------------------------
PAGES = [
    "1 · Disaster GeoAI",
    "2 · PalmCity 360°",
    "3 · SAR Crop Height",
    "4 · PolSAR Benchmark",
    "5 · AlphaEarth",
]
page = st.segmented_control("Portfolio module", PAGES, default=PAGES[0], key="portfolio_page")

if page == PAGES[0]:
    render_disaster()
elif page == PAGES[1]:
    render_palmcity()
elif page == PAGES[2]:
    render_crop_height()
elif page == PAGES[3]:
    render_foundation()
elif page == PAGES[4]:
    render_alphaearth()