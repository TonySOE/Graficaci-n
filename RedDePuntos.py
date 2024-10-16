import numpy as np 
import cv2 as cv

cap = cv.VideoCapture(0)


lkparm =dict(winSize=(15,15), maxLevel=2,
             criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03)) 


_, vframe = cap.read()
vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)
p0 = np.array([(100,100), (200,100), (300,100), (400,100), (500,100), (600,100),
               (100,200), (200,200), (300,200), (400,200), (500,200), (600,200),
               (100,300), (200,300), (300,300), (400,300), (500,300), (600,300),
               (100,400), (200,400), (300,400), (400,400), (500,400), (600,400)])

p0 = np.float32(p0[:, np.newaxis, :])

mask = np.zeros_like(vframe) 
cad =''

while True:
    _, frame = cap.read()
    fgris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    p1, st, err = cv.calcOpticalFlowPyrLK(vgris, fgris, p0, None, **lkparm) 

    if p1 is None:
        vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)
        p0 = np.array([(100,100), (200,100), (300,100), (400,100), (500, 100) ])
        p0 = np.float32(p0[:, np.newaxis, :])
        mask = np.zeros_like(vframe)
        cv.imshow('ventana', frame)
    else:
        bp1 = p1[st ==1]
        bp0 = p0[st ==1]
        
        for i, (nv, vj) in enumerate(zip(bp1, bp0)):
            a, b = (int(x) for x in nv.ravel())
            c, d = (int(x) for x in vj.ravel())
            dist = np.linalg.norm(nv.ravel() - vj.ravel())

            # Dibujar círculos en el punto actual y el punto anterior
            frame = cv.circle(frame, (c, d), 2, (255, 0, 0), -1)
            frame = cv.circle(frame, (a, b), 3, (0, 255, 0), -1)

            # Conectar el punto actual con sus vecinos cercanos
            for j, (nv2, vj2) in enumerate(zip(bp1, bp0)):
                if i != j:  # No conectar el punto consigo mismo
                    a2, b2 = (int(x) for x in nv2.ravel())
                    distancia_entre_puntos = np.linalg.norm(nv.ravel() - nv2.ravel())
                    if distancia_entre_puntos < 120:  # Distancia umbral para considerar puntos vecinos
                        frame = cv.line(frame, (a, b), (a2, b2), (0, 255, 255), 1)
                        
        cv.imshow('ventana', frame)

        vgris = fgris.copy()

        if(cv.waitKey(1) & 0xff) == 27:
            break

cap.release()
cv.destroyAllWindows()