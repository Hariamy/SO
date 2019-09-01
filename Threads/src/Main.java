import questao_1.ContadorCrescente;
import questao_1.ContadorDecrescente;
import questao_2.Corredor;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner terminal = new Scanner(System.in);
        System.out.print("Digite a questão desejada ou exit para sair: ");
        String escolha = terminal.nextLine();

        while (!escolha.equalsIgnoreCase("exit")) {
            if (escolha.equalsIgnoreCase("1")) {
                int ate = 100;
                ContadorDecrescente cont1 = new ContadorDecrescente("Decrescente T1", ate);
                ContadorDecrescente cont2 = new ContadorDecrescente("Decrescente T2", ate);

                ContadorCrescente cont3 = new ContadorCrescente("Crescente T3", ate);
                ContadorCrescente cont4 = new ContadorCrescente("Crescente T4", ate);
                Thread tcont3 = new Thread(cont3);
                Thread tcont4 = new Thread(cont4);

                cont1.start();
                cont2.start();
                tcont3.start();
                tcont4.start();
            }
            else if (escolha.equalsIgnoreCase("2")) {
                int trajeto = 20;
                Corredor cor1 = new Corredor("Corredor 1", trajeto, 1);
                Corredor cor2 = new Corredor("Corredor 2", trajeto, 2);
                Corredor cor3 = new Corredor("Corredor 3", trajeto, 3);
                Corredor cor4 = new Corredor("Corredor 4", trajeto, 4);

                cor1.start();
                cor2.start();
                cor3.start();
                cor4.start();
            }

            //System.out.print("Digite a questão desejada ou exit para sair: ");
            escolha = terminal.nextLine();
        }
    }
}
