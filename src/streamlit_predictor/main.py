import streamlit as st
from streamlit_sortables import sort_items
from streamlit_predictor.teams import teams_2025
import requests
import json

simple_style = """
/* 並び替えリストのスタイル */
.sortable-component {
    font-size: 16px;
    width: 300px;
    margin: 0 auto;
}

/* 各アイテムのスタイル */
.sortable-item {

    background-color: #f4f4f4;
    cursor: grab;
    color: #333;
}

/* ホバー時のエフェクト */
.sortable-item:hover {
    background-color: #e0e0e0;
}

"""

prediction = sort_items(teams_2025, direction="vertical", custom_style=simple_style)

name = st.text_input("お名前を入力してください (必須)", placeholder="山田 太郎")
email = st.text_input(
    "メールアドレスを入力してください (必須)", placeholder="predictor@gmail.com"
)
confidence = st.slider(
    "自信のレベルを選択してください (1: 最も自信ある, 5: 最も自信ない）", 1, 5, value=3
)
prediction_points = st.text_area(
    "予想のポイントを入力してください", placeholder="※任意", value=""
)
enthusiasm = st.text_area("意気込みを入力してください", placeholder="※任意", value="")

data = {
    "prediction": str(prediction),
    "name": name,
    "email": email,
    "confidence": confidence,
    "prediction_points": prediction_points,
    "enthusiasm": enthusiasm,
}


ready = name != "" and email != ""

if st.button("送信", disabled=not ready):

    response = requests.post(url=st.secrets["GAS_WEBHOOK_URL"], json=data)
    if response.json()["status"] == "success":
        st.success("送信成功! Google スプレッドシートに保存されました。")
    else:
        st.error(
            "送信失敗。もう一度やり直すか、管理者に以下の結果をそのまま送ってください。"
        )

    st.write(data)
