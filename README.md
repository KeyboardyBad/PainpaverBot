##封存
已經好久沒寫新東西給這個機器人了，是時候封存他了

# 說明
這是一個ㄐㄐDC機器人，他會做的事很少。

`gg3be0.py`是我收集統神文的地方，寫成list格式，不要機器人只要統神文的也可以。

# 前置作業
一定要安裝python3，以下步驟Windows沒有反應的話，要從Microsoft Store下載Python。

下載之後解壓縮，
打開終端機，移動到這個PainpaverBot的目錄：

`cd path/to/PainpaverBot`

然後建立一個虛擬環境，名稱舉例dc：

`python3 -m venv dc`

接下來啟動這個虛擬環境：

> 如果是Windows

`dc\Scripts\activate.bat`

> 如果是Unix/MacOS

`source dc/bin/activate`

最後用pip安裝discord.py：


大部分要改的變數都在程式很上面的地方，有用到的就改一改，沒用到的可以不改，但是我不知道會不會壞掉。

TOKEN一定要改就對了。

> 如果是Windows

`py -3 -m pip install -U discord.py`

> 如果是Unix/MacOS

`python3 -m pip install -U discord.py`

這樣應該就可以了。

# 啟動機器人
做完前置作業後，一樣移動到PainpaverBot的目錄並啟動虛擬環境，然後直接跑bot.py：

`python3 bot.py`

python3不行就用

`python bot.py`

大概就這樣，有bug再說。
