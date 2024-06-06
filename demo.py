import pandas as pd
import joblib

def getInput():
  while True:
    try: sex = input("Sex (M/F): ")
    except: continue

    if sex in ('F', 'f', '0'): sex = 0
    elif sex in ('M', 'm', '1'): sex = 1
    if sex in (0, 1): break

  while True:
    try: studyTime = float(input("How long did you study for the exam (in hours): "))
    except: continue

    if studyTime < 2: studyTime = 1
    elif studyTime >= 2 and studyTime <= 5: studyTime = 2
    elif studyTime > 5: studyTime = 3
    if studyTime in (1, 2, 3): break

  while True:
    try: freeTime = float(input("How often/much is your free time (scale from 1 to 3): "))
    except: continue

    freeTime = int(freeTime)
    if freeTime < 1: freeTime = 1
    elif freeTime > 3: freeTime = 3
    if freeTime in (1, 2, 3): break

  while True:
    try: romantic = input("Are you in any form of romantic relationship (yes/no): ")
    except: continue

    _romantic = romantic.lower()
    if _romantic in ('no', 'n', '0'): romantic = 0
    elif _romantic in ('yes', 'y', '1'): romantic = 1
    if romantic in (0, 1): break

  while True:
    try: weeklyAlcoIntake = float(input("How much alcohol do you consume weekly (scale from 1 to 4): "))
    except: continue

    weeklyAlcoIntake = int(weeklyAlcoIntake)
    if weeklyAlcoIntake < 1: weeklyAlcoIntake = 1
    elif weeklyAlcoIntake > 4: weeklyAlcoIntake = 4
    if weeklyAlcoIntake in (1, 2, 3, 4): break

  while True:
    try: goOut = float(input("How often/much do you go out (scale from 1 to 4): "))
    except: continue

    goOut = int(goOut)
    if goOut < 1: goOut = 1
    elif goOut > 4: goOut = 4
    if goOut in (1, 2, 3, 4): break

  while True:
    try: parentsEdu = float(input("Highest education level of your parents (scale from 1 to 4): "))
    except: continue

    parentsEdu = int(parentsEdu)
    if parentsEdu < 1: parentsEdu = 1
    elif parentsEdu > 4: parentsEdu = 4
    if parentsEdu in (1, 2, 3, 4): break

  while True:
    try: absences = float(input("Your absences in this course: "))
    except: continue

    absences = int(absences)
    if absences < 1: absences = 1
    elif absences > 7: absences = 7
    if absences in (1, 2, 3, 4, 5, 6, 7): break

  while True:
    try: reason = input("Your main reason for choosing to attend this school ('course' if course-related, 'reputation' if school reputation-related, 'home' if residency-related, or 'other'): ")
    except: continue

    _reason = reason.lower()
    if _reason in ('course', '0'): reason = 0
    if _reason in ('reputation', '1'): reason = 1
    if _reason in ('other', '2'): reason = 2
    if _reason in ('home', '3'): reason = 3
    if reason in (0, 1, 2, 3): break

  while True:
    try:
      finalGrade = input("(Optional) The grade you got for this exam (0-20, or press enter to skip): ")
      if finalGrade == '': finalGrade = -1
      else: finalGrade = float(finalGrade)
    except: continue

    if finalGrade == -1: break
    elif finalGrade < 0: finalGrade = 0
    elif finalGrade > 20: finalGrade = 20
    break

  while True:
    try:
      predictedGrade = input("(Optional) Enter a grade someone who saw all your input above will predict (1-20, or press enter to skip): ")
      if predictedGrade == '': predictedGrade = -1
      else: predictedGrade = float(predictedGrade)
    except: continue

    if predictedGrade == -1: break
    elif predictedGrade < 0: predictedGrade = 0
    elif predictedGrade > 20: predictedGrade = 20
    break

  while True:
    try: stereotypeActivation = input("(Optional) The stereotype activation of the predictor (0 or 'none', 1 or 'case-based', 2 or 'statistics', or press enter to skip): ")
    except: continue

    _stereotypeActivation = stereotypeActivation.lower()
    if stereotypeActivation == '':
      stereotypeActivation = -1
      break
    elif _stereotypeActivation in ('none', '0'): stereotypeActivation = 0
    elif _stereotypeActivation in ('case-based', 'casebased', 'case based', '1'): stereotypeActivation = 1
    elif _stereotypeActivation in ('statistics', 'statistic', '2'): stereotypeActivation = 2
    if stereotypeActivation in (0, 1, 2): break

  return {
      'Sex' : sex,
      'StudyTime' : studyTime,
      'FreeTime' : freeTime,
      'Romantic' : romantic,
      'WeeklyAlcoIntake' : weeklyAlcoIntake,
      'GoOut' : goOut,
      'ParentsEdu' : parentsEdu,
      'Absences' : absences,
      'Reason' : reason,
      'FinalGrade' : finalGrade,
      'PredictedGrade' : predictedGrade,
      'StereotypeActivation' : stereotypeActivation
  }

def predictHuman(inp):
  # Predict with human predictions
  inp = pd.DataFrame(inp, index=[0])
  return round(tunedModel.predict(inp))

def predictNoHuman(inp):
  # Predict with no human predictions
  inp = pd.DataFrame(inp, index=[0])
  return round(tunedModelNH.predict(inp))

if __name__ == "__main__":
  
  # Load the model
  modelPath = "./models/tunedModel.pkl"
  modelPathNH = "./models/tunedModelNH.pkl"
  tunedModel = joblib.load(modelPath)
  tunedModelNH = joblib.load(modelPathNH)

  # Get input  
  inp = getInput()
  finalGrade = inp.pop('FinalGrade')

  # Predict and print
  print()
  if inp['PredictedGrade'] != -1 and inp['StereotypeActivation'] != -1:
    predWithHuman = predictHuman(inp)
    print("Taking into account the human prediction, the model predicted you will have a grade of:", predWithHuman)
    if finalGrade != -1:
      print("This is", abs(finalGrade - predWithHuman), "off your actual grade.")
    print()

  inp.pop('PredictedGrade')
  inp.pop('StereotypeActivation')
  predNoHuman = predictNoHuman(inp)
  print("Disregarding the human prediction, the model predicted you will have a grade of:", predNoHuman)
  if finalGrade != -1:
    print("This is", abs(finalGrade - predNoHuman), "off your actual grade.")