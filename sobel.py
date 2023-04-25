import cv2 as cv

img = cv.imread('HyunWoo.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

grad_x = cv.Sobel(gray,cv.CV_32F,1,0,ksize=3) #소벨 연산자 적용
grad_y = cv.Sobel(gray,cv.CV_32F,0,1,ksize=3) #(src=입력영상, ddepth=출력 영상의 dtype(-1:이전영상과 동일), dx, dy(미분차수 0,1,2중 선택, 둘다 0일 수는 없음), ksize(커널의 크기(1,3,5,7중 선택)), scale(미분에 사용할 계수), delta(연산 결과에 가산할 값))

sobel_x = cv.convertScaleAbs(grad_x) #절대값을 취해 양수 영상으로 변환
sobel_y = cv.convertScaleAbs(grad_y) 

edge_strength = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0) #에지 강도 계산 가중치를 sobel_x에 0.5, sobel_y에 0.5로 합 계산, 교재에서는 root(sobel_x^2 + sobel_y^2)

cv.imshow('Original', gray)
cv.imshow('sobelx', sobel_x)
cv.imshow('sobely', sobel_y)
cv.imshow('edge strength', edge_strength)

cv.imwrite('sobel_x.jpg', sobel_x)
cv.imwrite('sobel_y.jpg', sobel_y)
cv.imwrite('edge_strength.jpg', edge_strength)

cv.waitKey()
cv.destroyAllWindows()