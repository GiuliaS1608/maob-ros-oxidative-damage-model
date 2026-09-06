% Projeto IC: Investigacao de MAO-B e Estresse Oxidativo
% Modelo baseado em Dopamina (S), H2O2 (H), ROS (R) e Dano Oxidativo (D)

clear all;
clc;
close all;

%% 1. DEFINICAO DO CENARIO

% Escolha uma das opcoes:
% 'Basal'
% 'MAOB_aumentada'
% 'Producao_dopamina_aumentada'
% 'Deficiencia_antioxidante'
% 'Reparo_reduzido'

cenario = 'Basal';


%% 2. PARAMETROS BASAIS DO MODELO

Km = 229;                  % Constante de Michaelis-Menten (uM)

Vmax_basal = 100;          % Velocidade maxima efetiva da reacao (uM/min)
P = 50;                    % Producao basal de dopamina (uM/min)
Ks = 0.7;                  % Remocao fisiologica adicional da dopamina (min^-1)

alpha = 1.0;               % Fator efetivo de formacao/conversao de H2O2
Kh = 0.5;                  % Remocao de H2O2 (min^-1)

beta = 0.8;                % Formacao efetiva de ROS (min^-1)
Kr = 0.7;                  % Neutralizacao de ROS (min^-1)

gamma = 0.6;               % Fator efetivo de formacao/conversao de dano
Kd = 0.9;                  % Reparo/remocao do dano oxidativo (min^-1)

Vmax_eff = Vmax_basal;


%% 3. ALTERACAO DOS PARAMETROS DE ACORDO COM O CENARIO

switch cenario

    case 'Basal'

        tempo_final = 10;


    case 'MAOB_aumentada'

        Vmax_eff = 500;
        tempo_final = 10;


    case 'Producao_dopamina_aumentada'

        P = 90;
        tempo_final = 10;


    case 'Deficiencia_antioxidante'

        Kh = 0.2;
        Kr = 0.3;
        tempo_final = 20;


    case 'Reparo_reduzido'

        Kd = 0.2;
        tempo_final = 20;


    otherwise

        error('Cenario nao reconhecido.');

end


%% 4. CONFIGURACAO NUMERICA

h = 0.05;                  % Passo temporal em minutos
                           % 0.05 min = 3 segundos

t = 0:h:tempo_final;

N = length(t);

% Matriz de variaveis:
%
% linha 1 -> S(t): dopamina, em uM
% linha 2 -> H(t): H2O2, em unidades arbitrarias
% linha 3 -> R(t): ROS, em unidades arbitrarias
% linha 4 -> D(t): dano oxidativo, em unidades arbitrarias

y = zeros(4, N);

S0 = 200;                  % uM
H0 = 0;                    % u.a.
R0 = 0;                    % u.a.
D0 = 0;                    % u.a.

y(:,1) = [S0; H0; R0; D0];


%% 5. SISTEMA DE EQUACOES DIFERENCIAIS

f = @(t,y) [

    P ...
    - (Vmax_eff * y(1) / (Km + y(1))) ...
    - Ks * y(1);

    alpha * (Vmax_eff * y(1) / (Km + y(1))) ...
    - Kh * y(2);

    beta * y(2) ...
    - Kr * y(3);

    gamma * y(3) ...
    - Kd * y(4)

];


%% 6. METODO DE RUNGE-KUTTA DE QUARTA ORDEM (RK4)

for i = 1:N-1

    k1 = f(t(i), y(:,i));

    k2 = f(t(i) + h/2, ...
           y(:,i) + (h/2)*k1);

    k3 = f(t(i) + h/2, ...
           y(:,i) + (h/2)*k2);

    k4 = f(t(i) + h, ...
           y(:,i) + h*k3);

    y(:,i+1) = y(:,i) ...
             + (h/6)*(k1 + 2*k2 + 2*k3 + k4);

end


%% 7. PLOTAGEM DOS RESULTADOS

figure;


subplot(2,2,1);

plot(t, y(1,:), 'b', 'LineWidth', 2);

title('Dinamica do substrato (Dopamina)');
xlabel('Tempo (min)');
ylabel('Concentracao de dopamina (\muM)');

grid on;
set(gca, 'FontSize', 9);


subplot(2,2,2);

plot(t, y(2,:), 'r', 'LineWidth', 2);

title('Producao de H_2O_2');
xlabel('Tempo (min)');
ylabel('Nivel de H_2O_2 (u.a.)');

grid on;
set(gca, 'FontSize', 9);


subplot(2,2,3);

plot(t, y(3,:), 'g', 'LineWidth', 2);

title('Formacao de ROS');
xlabel('Tempo (min)');
ylabel('Nivel de ROS (u.a.)');

grid on;
set(gca, 'FontSize', 9);


subplot(2,2,4);

plot(t, y(4,:), 'm', 'LineWidth', 2);

title('Acumulo de dano oxidativo');
xlabel('Tempo (min)');
ylabel('Dano oxidativo (u.a.)');

grid on;
set(gca, 'FontSize', 9);


%% 8. RESUMO DA SIMULACAO

fprintf('\n');
fprintf('Cenario: %s\n', cenario);
fprintf('Tempo final: %.1f min\n', tempo_final);
fprintf('\n');

fprintf('Valores finais:\n');
fprintf('S(t) = %.4f uM\n', y(1,end));
fprintf('H(t) = %.4f u.a.\n', y(2,end));
fprintf('R(t) = %.4f u.a.\n', y(3,end));
fprintf('D(t) = %.4f u.a.\n', y(4,end));
fprintf('\n');
