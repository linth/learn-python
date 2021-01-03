

class IeColor:
    """ the class is for printing information with color. """
    # color
    pink = '\033[95m'
    blue = '\033[94m'
    success = '\033[92m'
    warning = '\033[93m'
    red = '\033[91m'

    # style
    end = '\033[0m'
    bold = '\033[1m'
    under_line = '\033[4m'

    """
    examples:
        - add font color.
            30 ~ 37, i.e., \033[30m ~ \033[37m
        - add background color.
            40 ~ 47, i.e., \033[40;37m ~ \033[47;37m
    others:
        \33[0m 關閉所有屬性
        \33[1m 設置高亮度
        \33[4m 下劃線
        \33[5m 閃爍
        \33[7m 反顯
        \33[8m 消隱
        \33[30m -- \33[37m 設置前景色
        \33[40m -- \33[47m 設置背景色
        \33[nA 光標上移n行
        \33[nB 光標下移n行
        \33[nC 光標右移n行
        \33[nD 光標左移n行
        \33[y;xH設置光標位置
        \33[2J 清屏
        \33[K 清除從光標到行尾的內容
        \33[s 保存光標位置
        \33[u 恢復光標位置
        \33[?25l 隱藏光標
        \33[?25h 顯示光標 
    """
