package questao_1;

public class ContadorCrescente implements Runnable {
    int valor;
    String nome;

    public ContadorCrescente(String nome, int valor){
        this.valor = valor;
        this.nome = nome;
    }
    @Override
    public void run() {
        for (int i = 0; i <= valor; i++) {
            System.out.println(nome + ": " + i);
        }
    }
}
