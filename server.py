#coding:utf-8
from sanic import Sanic, response
from sanic.response import text

from get_life import YEAR_MAP, MONTH_MAP, DAY_MAP, HOUR, LIFE_MAP

app = Sanic(__name__)

@app.route("/")
async def test(request):
    return text('Hello world!')


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