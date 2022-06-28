def check_condition(gender, height, weight):
      if gender == "nu":
          if height >= 160 and weight >= 48:
              return True
          else:
              return False
      else:
          if height >= 165 and weight >= 54:
              return True
          else:
              return False

gender = "nu"
height = 200
weight = 70
answer = check_condition(gender, height, weight)
print(answer)