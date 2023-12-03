import streamlit as st

st.title("1ヶ月このペースで使い続けてもいいの？？チェッカー（1人～3人の家庭用）")
st.write("※すべて結果が出ますが、知りたい項目だけ入力してその結果にだけ注目してください。")
st.write("※使用している会社によって料金が違うのでおおよその目安として使って下さい")

st.write("　")
st.write("　")

mon = st.number_input("今は何月ですか？", min_value=1, max_value=12, value=7)
monn = str(mon)


if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
    daymax = 31
elif mon == 4 or mon == 6 or mon == 9 or mon == 11:
    daymax = 30
elif mon == 2:
    uru = st.selectbox("今年はうるう年ですか？", list({"はい", "いいえ"}))
    if uru == "はい":
        daymax = 29
    elif uru == "いいえ":
        daymax = 28

day = st.number_input("今日は何日ですか？", min_value=1, max_value=daymax, value=15)
dayy = str(day)
st.write("今日は" + monn + "月" + dayy + "日です。")

st.write("　")
st.write("　")
st.write("　")

st.markdown(f"## 今月の予算を入力してください。")
st.write("　")

budgas = st.slider("今月のガス代の予算(円)は？",0,20000,3000,100)
st.markdown(f"### ガス代の予算は" + str(budgas) + "(円)")
st.write("　")
budwat = st.slider("今月の水道代の予算(円)は？",0,20000,3000,100)
st.markdown(f"### 水道代の予算は" + str(budwat) + "(円)")
st.write("　")
budele = st.slider("今月の電気代の予算(円)は？",0,20000,3000,100)
st.markdown(f"### 電気代の予算は" + str(budele) + "(円)")
st.write("　")
budfoo = st.slider("今月の食費の予算(円)は？",0,60000,25000,100)
st.markdown(f"### 食費の予算は" + str(budfoo) + "(円)")
st.write("　")
budlif = st.slider("生活費などその他の出費",0,60000,25000,100)
st.markdown(f"### 生活費などその他の出費の予算は" + str(budlif) + "(円)")
st.write("　")
budall = st.slider("今月の合計（ガス・水道・電気代、食費、その他の合計）の予算(円)は？",0,150000,50000,100)
st.markdown(f"### 今月の合計の予算は" + str(budall) + "(円)")

st.write("　")
st.write("　")
st.write("　")
st.write("　")
st.write("　")
st.write("　")
st.markdown(f"## 今日までの使用量を教えてください")
st.write("　")

usegas = st.slider("今月のガス使用量(L)は？",0.0,10.0,2.0,0.1)
"ガス使用量(L):",usegas
usewat = st.slider("今月の水道使用量(L)は？",0.0,20.0,5.0,0.1)
"水道使用量(L):",usewat
useele = st.slider("今月の電気使用量(kWh)は？",0,400,100)
"電気使用量(kWh):",useele
usefoo = st.slider("今月使った食費(円)は？",0,60000,25000)
"食費(円):",usefoo
uselif = st.slider("今月にガス・水道・電気代、食費以外で使った金額(円)は？",0,150000,50000)
"その他の出費(円):",uselif

st.write("　")
st.write("　")
st.write("　")
st.write("　")
st.write("　")
st.write("　")
st.markdown(f"## 使用料金を教えてください（初めの値は平均の値段に設定しているので、分からない人は変更しなくて大丈夫です)")
st.write("　")

mongas = st.slider("1Lあたりのガス使用料金(円)は？",0,1000,700)
"1Lあたりのガス使用料金(円):",mongas
monwat = st.slider("1Lあたりの水道使用料金(円)は？",0,200,70)
st.write("（利用料によっても料金が変わりますが、一人暮らしなら利用料が変わることはほぼないので今回は入力するスペースを一つにします。）")
"1Lあたりの水道使用料金(円):",monwat
monele = st.slider("1kwhあたりの電気使用量は？",0,60,31)
"電気使用料金(円):",monele

st.write("　")
st.write("　")
st.write("　")
st.write("　")
st.write("　")
st.write("　")
st.title("このままのペースで使うと...")
st.write("　")

if (1820 + usegas * mongas) * daymax / day <= budgas:
    st.write("・「ガス」　このままのペースで使えば予算に収まります。")
if (1820 + usegas * mongas) * daymax / day > budgas:
    lastgas = str((1820 + usegas * mongas) * daymax / day - budgas)
    st.write("・「ガス」　このままのペースで使うと予算を" + lastgas + "円超えます。")

if (1200 + usewat * monwat) * daymax / day <= budwat:
    st.write("・「水道」　このままのペースで使えば予算に収まります。")
if (1200 + usewat * monwat) * daymax / day > budwat:
    lastwat = str((1200 + usewat * monwat) * daymax / day - budwat)
    st.write("・「水道」　このままのペースで使うと予算を" + lastwat + "円超えます。")

if (useele * monele) * daymax / day <= budele:
    st.write("・「電気」　このままのペースで使えば予算に収まります。")
if (useele * monele) * daymax / day > budele:
    lastele = str(-(budele - (useele * monele) * daymax / day))
    st.write("・「電気」　このままのペースで使うと予算を" + lastele + "円超えます。")

if usefoo * daymax / day <= budfoo:
    st.write("・「食費」　このままのペースで使えば予算に収まります。")
if usefoo * daymax / day > budfoo:
    lastfoo = str(-(budfoo - usefoo * daymax / day))
    st.write("・「食費」　このままのペースで使うと予算を" + lastfoo + "円超えます。")
    
if uselif * daymax / day <= budlif:
    st.write("・「その他」　このままのペースで使えば予算に収まります。")
if uselif * daymax / day > budlif:
    lastlif = str(-(budlif - uselif * daymax / day))                                                                           
    st.write("・「その他」　このままのペースで使うと予算を" + lastfoo + "円超えます。")

if ((1820 + usegas * mongas) + (1200 + usewat * monwat) + (useele * monele) + usefoo + uselif) * daymax / day <= budall:
    st.write("・「合計」　このままのペースで使えば予算に収まります。")
if ((1820 + usegas * mongas) + (1200 + usewat * monwat) + (useele * monele) + usefoo + uselif) * daymax / day > budall:
    lastall = str(-(budall - ((1820 + usegas * mongas) + (1200 + usewat * monwat) + (useele * monele) + usefoo + uselif) * daymax / day))
    st.write("・「合計」　このままのペースで使うと予算を" + lastall + "円超えます。")