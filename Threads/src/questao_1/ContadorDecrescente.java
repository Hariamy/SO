package questao_1;

public class ContadorDecrescente extends Thread {
    int valor;
    String nome;

    public ContadorDecrescente(String nome, int valor){
        this.valor = valor;
        this.nome = nome;
    }

    public void run(){
        for (int i = valor; i >= 0; i--) {
            System.out.println(nome + ": " + i);
        }
    }
}
