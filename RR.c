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
	// timequantum = 2, ABC ���� �ð� - 057,  execution time =17.10.14
	// ����ð� -> RR ���������� ����(Ÿ��Ȯ�ο�) -> ����LIST���� ->
	// RR ���μ��� ����Ȯ�ο� FCFS�� LIST, PCB meta�����ʿ�, Pointer, 
}	