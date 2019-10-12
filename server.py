#coding:utf-8
from sanic import Sanic, response
from sanic.response import text

from get_life import YEAR_MAP, MONTH_MAP, DAY_MAP, HOUR, LIFE_MAP

app = Sanic(__name__)

@app.route("/")
async def home(request):
    return text('称骨算命法，相传是唐朝周易大师袁天罡先生所创，其法将人的生辰八字，即出生的农历年月日时计算相应的“骨重”，然后根据“称骨”的总值来进行算命。(古代的重量单位：1斤=10两，1两=10钱)')


@app.route("/suan_ming",methods=["POST"])
async def post_data(request):
  year = request.args.get("year")
  month = request.args.get("month")
  day = request.args.get("day")
  hour = request.args.get("hour")
  try:
      score = YEAR_MAP[year] + MONTH_MAP[month] + DAY_MAP[day] + HOUR[hour]
      life_language = LIFE_MAP[str(int(score))]
      weight_list = str(score).split(".")
      life_weight = weight_list[0] + "两" + weight_list[1] + "钱"
  except:
      life_language,life_weight ="我命由我不由天！","0"
  return response.json(
        {'life_language': life_language,
         'life_weight':life_weight})

app.run(host="0.0.0.0", port=8000, debug=True)
