

from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    CarouselTemplate, CarouselColumn, MessageAction, TemplateSendMessage, TextSendMessage, MessageEvent, TextMessage, ButtonsTemplate, ImageSendMessage
)
from linebot.exceptions import InvalidSignatureError
from flask import Flask, request, abort

app = Flask(__name__)

line_bot_api = LineBotApi(
    'KFAf4SkL2mEt1UszoO6qzj4+4pfd2+uwoZXoLG+wzQUXWHHH4N5xDRyEBTTzhUsYOwfHqrplKitPS+O5UZ5GVCMamjWb/6+eAIZg8Id6MHRVUQMOq5NbMlAtSZ1w9Se5nnYD9pSuaRGc6rBv+mAV9AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5d14d94cef334ea90653efb3a803fc73')


def Breast_Cancer_Treatment_Process(event):  # 乳癌治療流程
    carousel_template = ImageSendMessage(
        original_content_url="https://drive.google.com/uc?export=view&id=1sJfu_L2yEJEYxHM2cR09ymykt-o0tqgp",
        preview_image_url="https://drive.google.com/uc?export=view&id=1sJfu_L2yEJEYxHM2cR09ymykt-o0tqgp"), TemplateSendMessage(
        alt_text='乳癌治療流程',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # thumbnail_image_url='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                    title='請選擇治療方法',
                    text='請選擇以下項目',
                    actions=[
                        MessageAction(
                            label='手術治療',
                            text='手術治療'
                        ),
                        MessageAction(
                            label='化學治療',
                            text='化學治療'
                        ),
                        MessageAction(
                            label='標靶治療',
                            text='標靶治療'
                        )
                    ]
                ),
                CarouselColumn(
                    # thumbnail_image_url='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                    title='請選擇治療方法',
                    text='請選擇以下項目',
                    actions=[
                        MessageAction(
                            label='放射線治療',
                            text='放射線治療'
                        ),
                        MessageAction(
                            label='抗荷爾蒙治療',
                            text='抗荷爾蒙治療'
                        ),
                        MessageAction(
                            label=' ',
                            text=' '
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, carousel_template)


def Rehabilitatio_Exercise_Instructions(event):  # 復健運動須知
    buttons_template = TemplateSendMessage(
        alt_text='復健運動須知',
        template=ButtonsTemplate(
            # thumbnail_image_url='https://example.com/image.jpg',
            title='復健運動須知',
            text='請選擇以下項目',
            actions=[
                MessageAction(
                    label='乳癌淋巴水腫之認識',
                    text='乳癌淋巴水腫之認識'
                ),
                MessageAction(
                    label='居家自我監測與預防淋巴水腫的認知',
                    text='居家自我監測與預防淋巴水腫的認知'
                ),
                MessageAction(
                    label='乳癌術後復健運動',
                    text='乳癌術後復健運動'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, buttons_template)


def Cancer_Resource_Center(event):  # 癌症資源中心
    buttons_template = TemplateSendMessage(
        alt_text='癌症資源中心',
        template=ButtonsTemplate(
            # thumbnail_image_url='https://example.com/image.jpg',
            title='癌症資源中心',
            text='請選擇以下項目',
            actions=[
                MessageAction(
                    label='假髮租借、頭巾購買',
                    text='假髮租借、頭巾購買'
                ),
                MessageAction(
                    label='假髮專賣店',
                    text='假髮專賣店'
                ),
                MessageAction(
                    label='義乳胸罩購買資訊',
                    text='義乳胸罩購買資訊'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, buttons_template)


def Surgical_treatment(event):  # 手術治療
    buttons_template = ImageSendMessage(
        original_content_url="https://drive.google.com/uc?export=view&id=1RvHaHRtIqTqSAlInqiPkFaBrveKmgNCB",
        preview_image_url="https://drive.google.com/uc?export=view&id=1RvHaHRtIqTqSAlInqiPkFaBrveKmgNCB"), TemplateSendMessage(
        alt_text='手術治療事項',
        template=ButtonsTemplate(
            # thumbnail_image_url='https://example.com/image.jpg',
            title='術前準備及術後傷口照護事項',
            text='請選擇以下項目',
            actions=[
                MessageAction(
                    label='術前準備',
                    text='術前準備'
                ),
                MessageAction(
                    label='術後傷口注意事項',
                    text='術後傷口注意事項'
                ),
                MessageAction(
                    label='術後可能合併症',
                    text='術後可能合併症'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, buttons_template)


def Rehabilitation(event):
    buttons_template = TemplateSendMessage(
        alt_text='乳癌術後復健運動',
        template=ButtonsTemplate(
            # thumbnail_image_url='https://example.com/image.jpg',
            title='乳癌術後復健運動',
            text='請選擇以下項目',
            actions=[
                MessageAction(
                    label='步驟一 腹式呼吸',
                    text='步驟一 腹式呼吸'
                ),
                MessageAction(
                    label='步驟二 一個星期內運動',
                    text='步驟二 一個星期內運動'
                ),
                MessageAction(
                    label='步驟三 一個月後的運動',
                    text='步驟三 一個月後的運動'
                ),
                MessageAction(
                    label='復健運動注意事項',
                    text='復健運動注意事項'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, buttons_template)


def Chemotherapy(event):  # 化療治療

    carousel_template = ImageSendMessage(
        original_content_url="https://drive.google.com/uc?export=view&id=11nUcIqhlJi40z8ZDWuZbFM1pPQzhcvRj",
        preview_image_url="https://drive.google.com/uc?export=view&id=11nUcIqhlJi40z8ZDWuZbFM1pPQzhcvRj"), TextSendMessage("\U0001F691化學治療會降低白血球數目，影響免疫力。如果在治療後出現以下症狀，應立即就醫：\n\n1. 發燒超過38°C、畏寒\n2. 上呼吸道感染症狀\U0001F637（咳嗽、流鼻水、喉嚨痛）\n3. 泌尿道感染（解尿疼痛、灼熱或解尿費力）\n4. 腸胃道感染（腹瀉一天3次以上、腹痛）\n\n\U0001F371飲食注意事項 ：\n\n1. 避免生食\U0001F363，多漱口以增強口腔清潔\U0001F9FD。口腔潰瘍者應進食軟質、無酸性食物\U0001F34C。\n2. 如果吃不下，可以飲食改為流質\U0001F9C3。\n3. 若有噁心、嘔吐\U0001F92E，治療\U0001FA79後1-2小時內減少食物攝取。可以喝一些水\U0001F6B0或食用溫或冷的食物、糖果\U0001F36C有幫助。\n4. 維持良好進食習慣有助於身體組織癒合。新鮮食物\U0001F966需徹底清洗和烹煮，選擇剝皮或削皮的水果。\n5. 避免生蛋\U0001F95A、發霉的乳酪\U0001F9C0和沙拉\U0001F957。使用較小的食物容器，每次食畢即丟棄剩餘食物。應使用個人進食器具，避免與他人共用以避免感染\U0001F637。"), TemplateSendMessage(
        alt_text='化學治療事項',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='化學治療',
                    text='請選擇以下項目',
                    actions=[
                        MessageAction(
                            label='如何處理口腔黏膜炎',
                            text='如何處理口腔黏膜炎'
                        ),
                        MessageAction(
                            label='如何處理噁心、嘔吐',
                            text='如何處理噁心、嘔吐'
                        ),
                        MessageAction(
                            label='如何處理腹瀉',
                            text='如何處理腹瀉'
                        )
                    ]
                ),
                CarouselColumn(
                    title='化學治療',
                    text='請選擇以下項目',
                    actions=[
                        MessageAction(
                            label='如何處理神經、關節、肌肉疼痛',
                            text='如何處理神經、關節、肌肉疼痛'
                        ),
                        MessageAction(
                            label='如何處理體液蓄積',
                            text='如何處理體液蓄積'
                        ),
                        MessageAction(
                            label=' ',
                            text=' '
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, carousel_template)


def Targeted_therapy(event):  # 標靶治療
    carousel_template = TextSendMessage("\U0001F3AF標靶治療是一種針對特定癌細胞生長因子發展出的藥物，它透過攻擊特定細胞表面的接受體來達到治療效果。\n這些藥物會阻斷細胞內的訊息傳遞，從而抑制乳癌細胞的分裂，延長患者的存活時間並減少癌症復發的風險。\n相較於化療，標靶藥物對其他正常細胞的傷害較小，因此副作用也較少。\n\n然而，並非每位乳癌患者都適合接受標靶治療，因為這種治療方式需要符合特定的病理特徵。\n當您符合標靶治療的條件時，醫生會主動提及並給予適合您病情的治療建議。"), TemplateSendMessage(
        alt_text='標靶治療事項',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='何謂標靶治療',
                    text='請選擇以下項目',  # 長度超過
                    actions=[
                        MessageAction(
                            label='HER-2行乳癌治療',
                            text='HER-2行乳癌治療'
                        ),
                        MessageAction(
                            label='CDK4/6抑制劑',  # (ER:+/HER-2:-)
                            text='CDK4/6抑制劑'  # (ER:+/HER-2:-)
                        ),
                        MessageAction(
                            label='抗血管新生藥物(HER-2:-)',
                            text='抗血管新生藥物(HER-2:-)'
                        )
                    ]
                ),
                CarouselColumn(
                    title='何謂標靶治療',
                    text='請選擇以下項目',
                    actions=[
                        MessageAction(
                            label='RARP抑制劑(BRCA1/2:+)',
                            text='RARP抑制劑(BRCA1/2:+)'
                        ),
                        MessageAction(
                            label='HER2標靶治療新劑型-皮下注射劑型',
                            text='HER2標靶治療新劑型-皮下注射劑型'
                        ),
                        MessageAction(
                            label=' ',
                            text=' '
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, carousel_template)


def radiation_therapy(event):  # 放射線治療
    buttons_template = TemplateSendMessage(
        alt_text='放射線治療',
        template=ButtonsTemplate(
            # thumbnail_image_url='https://example.com/image.jpg',
            title='放射線治療',
            text='請選擇以下項目',
            actions=[
                MessageAction(
                    label='乳癌放射線治療的適應症',
                    text='乳癌放射線治療的適應症'
                ),
                MessageAction(
                    label='放射線治療的準備工作',
                    text='放射線治療的準備工作'
                ),
                MessageAction(
                    label='放射線治療療程',
                    text='放射線治療療程'
                ),
                MessageAction(
                    label='放射線注意事項',
                    text='放射線注意事項'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, buttons_template)


def anti_hormonal_therapy(event):  # 抗荷爾蒙治療
    emoji = [
        {

            "index": 46,
            "productId": "5ac21b4f031a6752fb806d59",
            "emojiId": "053"
        },

        {
            "index": 107,
            "productId": "5ac21b4f031a6752fb806d59",
            "emojiId": "054"
        }
    ]

    message = TextSendMessage(
        text='\U0001F3E5抗荷爾蒙治療就是用藥物阻斷荷爾蒙接受體生成，達到疾病控制降低復發:目前最常見分兩類:\n\n$. 抗雌激素:最常見的泰莫西芬(Tamoxifen)，適用停經前、後賀爾蒙接受體陽性之病，至少服用2年可降低復發率。\n\n$. 降低雌激素生成，減少乳癌細胞生長，有2種:\n\n(1). 芳香環酶抑制劑(Aromatase Inhibitor，AI):主要用於停經後婦女，目前有3種藥物\U0001F48A復乳納、諾曼癌素、安美達錠\n(2).抑制黃體素分泌藥物(LHR):也就是停經針', emojis=emoji)
    line_bot_api.reply_message(event.reply_token, message)


def breast_cancer_lymphedema(event):  # 乳癌淋巴水腫之認識
    emoji = [
        {
            "index": 94,
            "productId": "5ac21b4f031a6752fb806d59",
            "emojiId": "054"

        }
    ]
    message = TextSendMessage(
        text='乳癌手術常需要摘除或擴清患側腋下的淋巴腺，並進行放射線治療，這可能影響淋巴循環，導致淋巴水腫。\n淋巴水腫的發生率與手術方式和是否進行放射線治療有關，大約在50%至56%之間。\n通常在手術後$年左右出現，表現為患側手臂腫脹、皮膚緊繃、手指僵硬、感覺異常等症狀。\n復健科醫師可以評估水腫程度並建議適當的復健運動\U0001F3C3。', emojis=emoji)
    line_bot_api.reply_message(event.reply_token, message)


def Prevent_Lymphedema(event):  # 居家自我監測與預防淋巴水腫的認知
    emoji = [
        {
            "index": 22,
            "productId": "5ac21b4f031a6752fb806d59",
            "emojiId": "053"
        },

        {
            "index": 162,
            "productId": "5ac21b4f031a6752fb806d59",
            "emojiId": "054"

        },
        {
            "index": 349,
            "productId": "5ac21b4f031a6752fb806d59",
            "emojiId": "055"

        }
    ]
    message = TextSendMessage(
        text='\U0001F3E1提供居家自我監測與預防淋巴水腫的認知 \n$. 高溫\U0001F525會使血管擴張而增加淋巴液產生 \n  (1). 避免蒸氣浴\U0001F9D6、泡溫泉、泡熱水澡，不刻意用熱水沖患者側手臂。 \n  (2). 避免使用紅外線、熱敷或深部按摩\U0001F486、推拿。 \n  (3). 避免長時間曝曬於太陽下或做日光浴\U0001F31E。 \n  (4). 天冷時避免使用電熱毯。\n\n$. 傷口會增加淋巴液產生 \n  (1). 避免於患者側手臂\U0001F4AA做抽血、打針\U0001F489、針灸等侵入性治療。 \n  (2). 小心保護患者側皮膚，避免蚊蟲\U0001F41B咬傷、外傷及皮膚乾裂而引發感染。 \n  (3). 天冷時避免皮膚乾裂，於患者側手臂上塗抹水溶性乳液\U0001F4A7。 \n  (4). 修剪指甲勿太短及需預防甲溝炎。 \n  (5). 於廚房工作時應小心．避免燙傷及使用刺激性之清潔劑。\n\n$. 減少干擾淋巴液回流 \n  (1). 避免各種會壓迫到患者側淋巴回流的首飾與配件(包括戒指\U0001F48D、手鐲或手錶等）。 \n  (2). 不要在患者側背、提、勾掛皮包或提超過3公斤的重物以及拖拉物品。 \n  (3). 避免穿戴過緊衣物，内衣胸罩應鬆緊適度調整，不要有鋼絲為佳。 \n  (4). 避免讓患者側上肢過度出力或做重複性極高動作 ，尤其會造成肢體痿痛或不適的行為要極力避免，痠痛可能會造成局部性發炎。 \n  (5). 保持適當體重及均衡、低鹽、高纖的飲食\U0001F360。', emojis=emoji)
    line_bot_api.reply_message(event.reply_token, message)


def Wig_rental_turban_purchase(event):  # 假髮租借、頭巾購買
    emoji = [
        {
            "index": 12,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "053"
        },
        {
            "index": 63,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "054"
        },
        {
            "index": 122,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "055"
        }
    ]
    message = TextSendMessage(
        text='假髮租借、頭巾購買:\n\n$. 高雄長庚醫院 癌症資源中心(07)731-7123分機3259\n\n醫學大樓7樓癌症中心門診區\n\n$. 癌症希望基金會 高雄小站(07)581-0661\n\n高雄市左營區翠峰路22號(押金500元，清潔費300元)\n\n$. 台灣癌症基金會 高雄服務中心 (07) 331-9137\n\n高雄市三民區九如二路150號9樓之1(押金1000元，清潔費300元)', emojis=emoji)
    line_bot_api.reply_message(event.reply_token, message)


def wig_store(event):  # 假髮專賣店
    emoji = [
        {
            "index": 7,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "053"
        },
        {
            "index": 18,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "027"
        },
        {
            "index": 55,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "028"
        },
        {
            "index": 91,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "054"
        },
        {
            "index": 129,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "055"
        },
        {
            "index": 173,
            "productId": "5ac21a8c040ab15980c9b43f",
            "emojiId": "056"
        },
        {
            "index": 185,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "027"
        },
        {
            "index": 224,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "028"
        },
        {
            "index": 264,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "029"
        },
        {
            "index": 302,
            "productId": "5ac21a8c040ab15980c9b43f",
            "emojiId": "057"
        },
        {
            "index": 316,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "027"
        },
        {
            "index": 354,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "028"
        },
        {
            "index": 393,
            "productId": "5ac21a8c040ab15980c9b43f",
            "emojiId": "058"
        }
    ]
    message = TextSendMessage(text='假髮專賣店\n\n$. 神奇假髮\n\n  $. 六合店 - (07)235-8866 高雄市六合一路101號\n\n  $. 新田店 - (07)216-2748 高雄市新田路195之2號\n\n$. 魔法部屋\n\n (07)224-9888 高雄市苓雅區中正二路70號\n\n$. 愛德蘭絲\n\n 高雄店 - (07)314-1035 高雄市左營區博愛三路18號\n\n$. 髮絲特假髮\n\n  $. 義華店 - (07)384-8071 高雄市三民區義華路157號\n\n  $. 九如店 - (07)380-6626 高雄市三民區九如一路858號\n\n  $. 六和店 - (07)236-1792 高雄店新興區六合一路168號\n\n$. C.Y.S假髮\n\n  $. 五福店 - (07)211-6699 高雄店前金區福三路60號\n\n  $. 三多店 - (07)338-8920 高雄市三多三路200號2樓之1\n\n$. 斯菲爾\n\n (07)229-9101 高雄市新興區中正二路162號', emojis=emoji)
    line_bot_api.reply_message(event.reply_token, message)


def breast_augmentation(event):  # 義乳胸罩購買資訊
    emoji = [
        {
            "index": 11,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "053"
        },
        {
            "index": 50,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "054"
        },
        {
            "index": 94,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "055"
        },
        {
            "index": 121,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "056"
        },
        {
            "index": 162,
            "productId": "5ac21a13031a6752fb806d57",
            "emojiId": "057"
        }
    ]
    message = TextSendMessage(text='義乳胸罩購買資訊 \n\n$. 虹坊國際有限公司 \n\n林嫦瑜 0912-359874 (採預約制) \n\n$. 華歌爾利曼馬系列 \n\n(07)223-6558 高雄市中正二路182號11樓 \n\n$. 夢娜義乳 \n\n吳小姐0939-714966 \n\n$. 勇承內衣 \n\n黃素丹0915-898392 高雄市三民區歸綬街129號 \n\n$. 禮黛內衣(黛莉貝爾) \n\n(07)310-5508 高雄市三民區明誠一路222號 陳美華 0937-386581 屏東市廈門街126號', emojis=emoji)
    line_bot_api.reply_message(event.reply_token, message)


def index():
    name = request.args.get('name')
    if name == None:  # <--有沒傳入任何url的參數
        # <--防止 "Hello"+name 出現 TypeError: can only concatenate str (not "NoneType") to str
        name = ""
    return "Hello"+name


@app.route("/linebot", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == '乳癌治療流程':
        Breast_Cancer_Treatment_Process(event)

    elif event.message.text == '手術治療':
        Surgical_treatment(event)

    elif event.message.text == '術前準備':
        emoji = [
            {
                "index": 0,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "053"
            },
            {
                "index": 45,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "054"
            },
            {
                "index": 82,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "055"
            }
        ]
        message = TextSendMessage(
            "$. 術前醫師會安排相關檢查，於手術前完成，完成後會與醫師討論術式及安排手術日期\U0001F4C5。\n\n$. 若平日有服用藥物\U0001F48A，例如抗凝血劑，心臟病用藥，請主到告知醫師。\n\n$. 請準備前開式上衣，方便手術後穿脫。", emojis=emoji)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '術後傷口注意事項':
        emoji = [
            {
                "index": 0,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "053"
            },
            {
                "index": 62,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "054"
            },
            {
                "index": 81,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "055"
            },
            {
                "index": 103,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "056"
            },
            {
                "index": 119,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "057"
            },
            {
                "index": 145,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "003"
            }
        ]
        message = TextSendMessage(
            "$. 每日應觀察傷口1~2次，注意傷口或周圍皮膚有無分泌物、紅、腫、熱、痛有無化膿情形，若有上述情形，應立即告知醫護人員\n\n$. 保持傷口及周圍皮膚的清潔\U0001F9FD\n\n$. 早期下床活動\U0001F3C3，以利傷口早期癒合\n\n$. 勿於傷口處塗擦其他藥品\n\n$. 多補充蛋白質，如:蛋\U0001F95A、奶\U0001F95B、魚肉類維生素$，如:柳橙\U0001F34A、奇異果\U0001F95D等", emojis=emoji)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '術後可能合併症':

        emoji = [
            {
                "index": 133,
                "productId": "5ac21e6c040ab15980c9b444",
                "emojiId": "001"
            }
        ]

        message = TextSendMessage(
            "一般而言、手術後有可能會發生的合併症包含：\n傷口感染\U0001F637、傷口出血\U0001FA78、傷口壞死等，但額外需要注意的是術後患部的發生乳癌術後患者大約有60-70%會出現患部血清腫、處理方式則回診時由醫師評估血清腫程度，再決定是否進行抽吸將組織液抽除、有時候會需要分次抽液才能漸進改善$。", emojis=emoji)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '化學治療':
        Chemotherapy(event)

    elif event.message.text == '如何處理口腔黏膜炎':
        emoji = [
            {
                "index": 0,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "053"
            },
            {
                "index": 41,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "054"
            },
            {
                "index": 79,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "055"
            },
            {
                "index": 102,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "056"
            },
            {
                "index": 133,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "057"
            },
            {
                "index": 151,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "058"
            },
            {
                "index": 178,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "059"
            },
            {
                "index": 226,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "060"
            },
            {
                "index": 279,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "061"
            }
        ]
        message = TextSendMessage("$. 攝取質地軟的食物，如：蛋\U0001F95A加燕麥\U0001F963、濃湯\U0001F372、冰淇淋\U0001F366、布丁\U0001F36E。\n\n$. 避免抽煙\U0001F6AC、喝酒\U0001F6AC、油炸及刺激性食物，如：咖啡、辛辣食物\U0001F336。\n\n$. 避免食用大量鹽分\U0001F9C2、酒精性漱口水。\n\n$. 避免用硬毛牙刷或牙線，傷害口腔，可使用軟毛牙刷刷牙。\n\n$. 嘴唇乾燥，可用護唇膏\U0001F484。\n\n$. 減少食用高溫食物\U0001F35C，應放涼至常溫後再食用。\n\n$. 進食後應立即漱口，以去除食物殘渣\U0001F990及細菌\U0001F9A0，並隨時維持口腔衛生\U0001F9FB以促進傷口癒合。\n\n$. 補充維生素、天然的食物，胚，芽米、糙米、雜糧飯、全麥麵包\U0001F35E、深綠色蔬菜\U0001F96C等是富含B群的食物。\n\n$. 若要使用健康食品請諮詢主治醫師\U0001FA7A後，再行使用。", emojis=emoji)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '如何處理噁心、嘔吐':
        emoji = [
            {
                "index": 0,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "053"
            },
            {
                "index": 28,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "054"
            },
            {
                "index": 51,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "055"
            },
            {
                "index": 75,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "056"
            },
            {
                "index": 96,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "057"
            },
            {
                "index": 118,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "058"
            }
        ]
        message = TextSendMessage(
            "$. 少量多餐\U0001F371、細嚼慢嚥，避免讓胃有過度飽脹感。\n\n$. 液體食物\U0001F9C3最好在餐前或餐後一小時。\n\n$. 避免用餐時\U0001F37D，攝取過多液體食物\U0001F964。\n\n$. 避免甜食\U0001F370、油炸、高脂肪食物。\n\n$. 攝取乾得食物，如烤麵包\U0001F35E、餅乾。\n\n$. 飯後坐著休息至少30分鐘，不要立即平躺。", emojis=emoji)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '如何處理腹瀉':
        emoji = [
            {
                "index": 0,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "053"
            },
            {
                "index": 22,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "054"
            },
            {
                "index": 36,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "055"
            },
            {
                "index": 48,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "056"
            },
            {
                "index": 68,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "057"
            }
        ]
        message = TextSendMessage(
            "$. 採清淡的液體食物\U0001F9C3，減輕胃負擔。\n\n$. 適當補充水份\U0001F6B0。\n\n$. 少量多餐\U0001F37D。\n\n$. 牛奶\U0001F95B或奶製品暫時不要服用。\n\n$. 避免吃刺激或產氣食物，如：咖啡、豆類及甜食\U0001F370。", emojis=emoji)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '如何處理神經、關節、肌肉疼痛':
        emoji = [
            {
                "index": 0,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "053"
            },
            {
                "index": 23,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "054"
            },
            {
                "index": 43,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "055"
            },
            {
                "index": 66,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "056"
            },
            {
                "index": 95,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "057"
            },
            {
                "index": 113,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "058"
            },
            {
                "index": 139,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "059"
            },
            {
                "index": 151,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "060"
            }
        ]
        message = TextSendMessage(
            "$. 神經性的副作用通常恢復的比較慢\U0001F915。\n\n$. 太燙的\U0001F525、尖銳的物品不要拿。\n\n$. 上下樓梯及走路\U0001F6B6時，最好請人扶持。\n\n$. 經常伸展末梢肢體\U0001F646，避免穿滑鞋子或高跟鞋\U0001F460。\n\n$. 浴室地板\U0001F6C1要鋪上防滑墊。\n\n$. 可臥床休息\U0001F634等恢復體力 ，進行活動\U0001F3C3。\n\n$. 採間歇性熱敷。\n\n$. 依醫囑給予適當的止痛劑\U0001F48A。", emojis=emoji)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '如何處理體液蓄積':
        emoji = [
            {
                "index": 0,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "053"
            },
            {
                "index": 48,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "071"
            },
            {
                "index": 65,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "054"
            }
        ]
        message = TextSendMessage(
            "$. 這與藥物\U0001F48A的累積劑量有關，通常發生在數個治療週期\U0001F501之後，若按醫囑服用類固醇，通常只有6$的病患會出現嚴重的體液滯留。\n\n$. 症狀包括：水腫、體重增加，少數患者會出現肋膜積液、腹水或心包膜積水\U0001F4A7，必要時可給予利尿劑來改善這個現象。", emojis=emoji)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '標靶治療':
        Targeted_therapy(event)

    elif event.message.text == 'HER-2行乳癌治療':

        message = ImageSendMessage(
            original_content_url="https://drive.google.com/uc?export=view&id=1-l22D3FTOJYve4UOcjSN9K2OoxFhXk5Q",
            preview_image_url="https://drive.google.com/uc?export=view&id=1-l22D3FTOJYve4UOcjSN9K2OoxFhXk5Q"),
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == 'CDK4/6抑制劑':

        message = TextSendMessage(
            "抗荷爾蒙標靶藥物，針對賀爾蒙受體陽性患者\U0001F915，目前有3種藥物\U0001F48A(Abemaciclib、Palbociclib、Ribociclib、Ribociclib)")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '抗血管新生藥物(HER-2:-)':

        message = TextSendMessage("\U0001F94A對抗人類血管內皮生長因子(VEGF)，如Bevacizumab")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == 'RARP抑制劑(BRCA1/2:+)':

        message = TextSendMessage(
            "用來治療BRCA基因突變局部晚期或轉移性乳癌患者\U0001F915，目前有Olaparib、Talazoparib")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == 'HER2標靶治療新劑型-皮下注射劑型':

        message = ImageSendMessage(
            original_content_url="https://drive.google.com/uc?export=view&id=1SmivCdTIJ9jzxoWSC7cRmY7Xyml6Zpso",
            preview_image_url="https://drive.google.com/uc?export=view&id=1SmivCdTIJ9jzxoWSC7cRmY7Xyml6Zpso")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '放射線治療':
        radiation_therapy(event)

    elif event.message.text == '抗荷爾蒙治療':
        anti_hormonal_therapy(event)

    elif event.message.text == '乳癌放射線治療的適應症':
        emoji = [
            {
                "index": 13,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "053"
            },
            {
                "index": 25,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "054"
            },
            {
                "index": 37,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "055"
            }
        ]
        message = TextSendMessage(
            "乳癌放射線治療的適應症\n\n$. 部分乳房切除。\n\n$. 原發腫瘤較大。\n\n$. 有淋巴轉移。\n\n其他：如手術切除標本邊緣仍有癌細胞侵犯，淋巴血管己有癌細胞\U0001F9EB侵犯，荷爾蒙受體陰性等.高危險因子。", emojis=emoji)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '放射線治療的準備工作':

        message = TextSendMessage(
            "製作固定身體的模具，注意不要照到手，所以手要向上舉\U0001F646。")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '放射線治療療程':
        emoji = [
            {
                "index": 9,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "053"
            },
            {
                "index": 32,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "054"
            },
            {
                "index": 57,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "055"
            }
        ]
        message = TextSendMessage(
            "放射線治療療程\n\n$. 星期一到星期五，每天到醫院接受照射。\n\n$. 總共28~35次，醫師依照病情決定次數。\n\n$.不會痛、沒有感覺。", emojis=emoji)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '放射線注意事項':
        emoji = [
            {
                "index": 9,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "053"
            },
            {
                "index": 66,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "054"
            },
            {
                "index": 109,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "055"
            },
            {
                "index": 152,
                "productId": "5ac21a13031a6752fb806d57",
                "emojiId": "056"
            }
        ]
        message = TextSendMessage(
            "放射線注意事項\n\n$. 應避免照射部位暴露於陽光下，如果在陽光下會超過十五分鐘時應做好防曬措施如著長袖長褲\U0001F456、戴帽子、撐傘等。\n\n$. 切勿使照射部位接觸冷源、熱源\U0001F525，如：冰水\U0001F9CA、熱水袋、熱水瓶、燈管\U0001F4A1等。\n\n$. 治療期間避免在鹹水或加人工消毒劑的游泳池中游泳\U0001F3CA，以免皮膚發紅、癢等現象。\n\n$. 治療期間及治療後半年內不要懷孕，因為放射線可能會影響胎兒\U0001F476。\n\n請放心，放射線治療後不會殘留在身體，可以正常抱老公、小孩\U0001F466喔。", emojis=emoji)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '復健運動須知':
        Rehabilitatio_Exercise_Instructions(event)

    # elif event.message.text == '乳癌淋巴水腫之認識':
    #     emoji = [
    #         {
    #             "index": 9,
    #             "productId": "5ac21a13031a6752fb806d57",
    #             "emojiId": "053"
    #         },
    #         {
    #             "index": 66,
    #             "productId": "5ac21a13031a6752fb806d57",
    #             "emojiId": "054"
    #         },
    #         {
    #             "index": 109,
    #             "productId": "5ac21a13031a6752fb806d57",
    #             "emojiId": "055"
    #         },
    #         {
    #             "index": 152,
    #             "productId": "5ac21a13031a6752fb806d57",
    #             "emojiId": "056"
    #         }
    #     ]
    #     message = TextSendMessage(
    #         "放射線注意事項\n\n$. 應避免照射部位暴露於陽光下，如果在陽光下會超過十五分鐘時應做好防曬措施如著長袖長褲\U0001F456、戴帽子、撐傘等。\n\n$. 切勿使照射部位接觸冷源、熱源\U0001F525，如：冰水\U0001F9CA、熱水袋、熱水瓶、燈管\U0001F4A1等。\n\n$. 治療期間避免在鹹水或加人工消毒劑的游泳池中游泳\U0001F3CA，以免皮膚發紅、癢等現象。\n\n$. 治療期間及治療後半年內不要懷孕，因為放射線可能會影響胎兒\U0001F476。\n\n請放心，放射線治療後不會殘留在身體，可以正常抱老公、小孩\U0001F466喔。", emojis=emoji)
    #     line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '乳癌淋巴水腫之認識':
        breast_cancer_lymphedema(event)

    elif event.message.text == '居家自我監測與預防淋巴水腫的認知':
        Prevent_Lymphedema(event)

    elif event.message.text == '乳癌術後復健運動':
        Rehabilitation(event)

    elif event.message.text == '步驟一 腹式呼吸':
        message = ImageSendMessage(
            original_content_url="https://drive.google.com/uc?export=view&id=1rnosUMUBEHKQQuJhXpOmruiKnBtG8qVr",
            preview_image_url="https://drive.google.com/uc?export=view&id=1rnosUMUBEHKQQuJhXpOmruiKnBtG8qVr")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '步驟二 一個星期內運動':
        message = TemplateSendMessage(
            alt_text='步驟二 一個星期內運動',
            template=ButtonsTemplate(
                title='步驟二 一個星期內可以執行的運動',
                text='請選擇以下項目',
                actions=[
                    MessageAction(
                        label='手掌運動',
                        text='手掌運動'
                    ),
                    MessageAction(
                        label='手腕屈曲運動',
                        text='手腕屈曲運動'
                    ),
                    MessageAction(
                        label='手肘灣曲運動',
                        text='手肘灣曲運動')
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '手掌運動':
        message = ImageSendMessage(
            original_content_url="https://drive.google.com/uc?export=view&id=1uPx0g9tYrmwnURGl4kAnTIeYUGtZ2Bxo",
            preview_image_url="https://drive.google.com/uc?export=view&id=1uPx0g9tYrmwnURGl4kAnTIeYUGtZ2Bxo")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '手腕屈曲運動':
        message = ImageSendMessage(
            original_content_url="https://drive.google.com/uc?export=view&id=13pglR4R4DfD4D387EiDY11BdnHKTws10",
            preview_image_url="https://drive.google.com/uc?export=view&id=13pglR4R4DfD4D387EiDY11BdnHKTws10")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '手肘灣曲運動':
        message = ImageSendMessage(
            original_content_url="https://drive.google.com/uc?export=view&id=1K-9pkJcwN812glLv5EjgGfHcQlOzf4R6",
            preview_image_url="https://drive.google.com/uc?export=view&id=1K-9pkJcwN812glLv5EjgGfHcQlOzf4R6")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '步驟三 一個月後的運動':
        message = TemplateSendMessage(
            alt_text='步驟三 一個月後的運動',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        # thumbnail_image_url='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                        title='步驟三 一個月後可以執行的運動',
                        text='請選擇以下項目',
                        actions=[
                            MessageAction(
                                label='肩關節屈曲運動',
                                text='肩關節屈曲運動'
                            ),
                            MessageAction(
                                label='肩甲骨外展及穩定運動',
                                text='肩甲骨外展及穩定運動'
                            ),
                            MessageAction(
                                label='滑牆運動',
                                text='滑牆運動'
                            )
                        ]
                    ),
                    CarouselColumn(
                        # thumbnail_image_url='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                        title='步驟三 一個月後可以執行的運動',
                        text='請選擇以下項目',
                        actions=[
                            MessageAction(
                                label='患肢擴胸運動',
                                text='患肢擴胸運動'
                            ),
                            MessageAction(
                                label='手臂旋轉運動',
                                text='手臂旋轉運動'
                            ),
                            MessageAction(
                                label=' ',
                                text=' '
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '肩關節屈曲運動':
        message = ImageSendMessage(
            original_content_url="https://drive.google.com/uc?export=view&id=1tSXwwxAqk5RiagUDChUr0Tk8HKQ1Rafv",
            preview_image_url="https://drive.google.com/uc?export=view&id=1tSXwwxAqk5RiagUDChUr0Tk8HKQ1Rafv")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '肩甲骨外展及穩定運動':
        message = ImageSendMessage(
            original_content_url="https://drive.google.com/uc?export=view&id=1VXchs9b9XZ5qmZow5HZKjFWGAXbcONvt",
            preview_image_url="https://drive.google.com/uc?export=view&id=1VXchs9b9XZ5qmZow5HZKjFWGAXbcONvt")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '滑牆運動':
        message = ImageSendMessage(
            original_content_url="https://drive.google.com/uc?export=view&id=1xPEQFfiYmFFRSSp0L7LTpeLVgbPuAzQN",
            preview_image_url="https://drive.google.com/uc?export=view&id=1xPEQFfiYmFFRSSp0L7LTpeLVgbPuAzQN")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '患肢擴胸運動':
        message = ImageSendMessage(
            original_content_url="https://drive.google.com/uc?export=view&id=1jCqG170ixUDwIC1wg2p2pRrqjO14cctA",
            preview_image_url="https://drive.google.com/uc?export=view&id=1jCqG170ixUDwIC1wg2p2pRrqjO14cctA")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '手臂旋轉運動':
        message = ImageSendMessage(
            original_content_url="https://drive.google.com/uc?export=view&id=1rFIy0S7dlA-e8_vTl9UD__YYTNEeJ3uL",
            preview_image_url="https://drive.google.com/uc?export=view&id=1rFIy0S7dlA-e8_vTl9UD__YYTNEeJ3uL")
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '復健運動注意事項':
        emoji = [
            {
                "index": 0,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "053"
            },
            {
                "index": 70,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "054"
            },
            {
                "index": 108,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "055"
            },
            {
                "index": 188,
                "productId": "5ac21a8c040ab15980c9b43f",
                "emojiId": "056"
            }
        ]
        message = TextSendMessage(
            text='$. 當您在做任何一項復健運動時患肢若感到疼痛加劇、或無法順利完成其中一項復健運動時都必須告知您的醫療團隊，以便重新評估體能並調整運動。\n\n$. 復健運動每天至少執行四次、每項運動需做20下才算是完整的復健運動。\n\n$. 術後初期復原運動，例如淋巴復健運動，可顯著減少術後併發症及淋巴水腫並加速復原，旦在術後接受化療或放療期間的持續運動訓練可有效降低癌疲憊與淋巴水腫情況。\n\n$. 目前乳癌手術標準治療方式均改採前哨淋巴腺偵測，可以有效降低淋巴水腫的發生率。如淋巴水腫真的發生，也不必過於擔心，經適當復健治療及處理，多數可獲得改善。手術後的復健運動是預防淋巴水腫發生的主要方式，一定要確實執行 •並注意觀察患側是否有腫脹的情形，如有任何不適皆須與主治醫師說明或尋求介復健科，才能及早發現及早治療。', emojis=emoji)

        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '癌症資源中心':
        Cancer_Resource_Center(event)

    elif event.message.text == '假髮租借、頭巾購買':
        Wig_rental_turban_purchase(event)

    elif event.message.text == '假髮專賣店':
        wig_store(event)

    elif event.message.text == '義乳胸罩購買資訊':
        breast_augmentation(event)

    else:
        reply = '請重新點選事項'
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=reply))


if __name__ == "__main__":
    app.run()
