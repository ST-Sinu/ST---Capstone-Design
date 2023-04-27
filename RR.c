#include <stdio.h>
#define END_TIME 1000

int main() {
	int time = 0;

	while (time <= END_TIME)
	{
		create_processes(time); // read events.txt
		round_robin();

		time++;
	}
}

void round_robin() {
	// timequantum = 2, ABC 시작 시간 - 057,  execution time =17.10.14
	// 현재시간 -> RR 지역변수에 저장(타임확인용) -> 다음LIST실행 ->
	// RR 프로세스 순서확인용 FCFS용 LIST, PCB meta변수필요, Pointer, 
}	