package questao_2;

public class Corredor extends Thread {
    String nome;
    int trajeto;
    int descanso;

    public Corredor(String nome, int trajeto, int descanso) {
        this.nome = nome;
        this.trajeto = trajeto;
        this.descanso = descanso;
    }

    public void run() {
        for (int i = trajeto; i > 0; i--) {
            System.out.println("Faltam " + i + " para o " + nome);
            try {
                System.out.println(nome + "está descansando");
                sleep(descanso*1000);
            }
            catch (InterruptedException e) {
                System.out.println(e);
            }
        }
        System.out.println(nome + " ---- Chegou!");
    }
}
