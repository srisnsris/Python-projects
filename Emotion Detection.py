from fer import FER

detector =  FER()
results = detector.detect_emotions('https://www.google.com/search?q=happy+images&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjLjIa17Z38AhXRl2oFHcbWCm0Q_AUoAXoECAMQAw&biw=1524&bih=751&dpr=1.05#imgrc=WfD9TSZmji4N9M')

emotion, score = detector.top_emotion('https://www.google.com/search?q=happy+images&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjLjIa17Z38AhXRl2oFHcbWCm0Q_AUoAXoECAMQAw&biw=1524&bih=751&dpr=1.05#imgrc=WfD9TSZmji4N9M')
print(emotion, score)