import streamlit as st
from streamlit_drawable_canvas import st_canvas
import time
import pandas as pd
def keisan():
    K_list = {
        "(-3)^2":"9",
        "2x+3x":"5x",
        "5x×3":"15x",
        "0.3×100":"30",
        "314-312": "2"}
    d = ["9", "5x", "15x", "30", "2"]
    answer_1 = "a"
    answer_2 = "b"
    answer_3 = "c"
    answer_4 = "d"
    answer_5 = "e"
    count = 0
    st.title("計算問題:sunglasses:")
    
    st.header("こちらは計算問題のデモだよ。下に解答用紙があるので半角で入力してみよう。満点だと風船がたくさん飛ぶよ。頑張ろう！")
    for Q,A in K_list.items(): 
        st.latex(Q)
    answer_1 = st.text_input('答え',"a")
    st.write('あなたの解答は', answer_1)
    answer_2 = st.text_input('答え',"b")
    st.write('あなたの解答は', answer_2)
    answer_3 = st.text_input('答え',"c")
    st.write('あなたの解答は', answer_3)
    answer_4 = st.text_input('答え',"d")
    st.write('あなたの解答は', answer_4)
    answer_5 = st.text_input('答え',"e")
    st.write('あなたの解答は', answer_5)
    if st.button('提出'):
        List = [answer_1,answer_2,answer_3,answer_4,answer_5]
        for i in range(5):
            if d[0] == List[0]:
                st.write("正解")
                count +=1
                if count == 5:
                    st.balloons()
            else:
                st.write("不正解")
        st.title("あなたの点数は５点中{} 点です！".format(count))
def render_gup():
    st.title("問題を作る！:sunglasses:")
    st.header('ここで問題を作ることができるよ。ただし、数式はプログラミングで入力しないと受け取れないよ。チェックを押して正しくできているか確認してから送信してね。')
    a = "/times" 
    b = "/div"     
    c = "/frac" 
  
    df = pd.DataFrame({
        '数式': ["＋","-","×", "÷","分数"],
       'command': ["+" ,"-" ,a,b,c],
        '使用例': ["x+3" ,"5-4" ,"2{}3".format(a),"6\div2","\ frac{x^3+1}{x+1}"]})
    st.table(df)
    st.header("複雑な記号を使いたい人は(http://www1.kiy.jp/~yoka/LaTeX/latex.html)へ！")
    suusiki = st.text_input('数式を入力してね',"(3x)^2")
    kotae = st.text_input('答えを入力してね', "９x^2")
    if st.button('チェック'):
        st.latex(suusiki)
        st.latex(kotae)
    if st.button('登録！'):
        with st.spinner('ちょっとまってね'):
             time.sleep(5)
             st.success('登録完了')
             st.balloons()
def main():
    # アプリケーション名と対応する関数のマッピング
    apps = {
        'スタートページ': None,
        '問題を作る！': render_gup,
        '計算問題を解く': keisan,
    }
    selected_app_name = st.sidebar.selectbox(label='apps',
                                             options=list(apps.keys()))

    if selected_app_name == 'スタートページ':
        st.title('Math リーグ:sunglasses:')
        st.header("これはデモです。私達の考えたMathリーグを実際に体験して少しでもイメージしてもらえたら幸せです。")
        st.info('左のバーから何をするか選んでね')
        st.stop()

    # 選択されたアプリケーションを処理する関数を呼び出す
    render_func = apps[selected_app_name]
    render_func()
if __name__ == '__main__':
    main()