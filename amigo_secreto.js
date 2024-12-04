class AmigoSecreto {
    constructor() {
        this.participantes = [];
        this.sorteio = new Map();
    }

    adicionarParticipante(nome) {
        nome = nome.trim();
        if (!nome) {
            alert("Por favor, digite um nome!");
            return false;
        }
        if (this.participantes.includes(nome)) {
            alert("Este participante já foi adicionado!");
            return false;
        }
        this.participantes.push(nome);
        return true;
    }

    realizarSorteio() {
        if (this.participantes.length < 3) {
            alert("É necessário pelo menos 3 participantes!");
            return false;
        }

        // Limpar sorteio anterior
        this.sorteio.clear();

        // Criar cópia dos participantes para sorteio
        let sorteados = [...this.participantes];

        // Realizar o sorteio
        for (let participante of this.participantes) {
            let sorteado;
            do {
                const indice = Math.floor(Math.random() * sorteados.length);
                sorteado = sorteados[indice];
            } while (sorteado === participante && sorteados.length > 1);

            this.sorteio.set(participante, sorteado);
            sorteados = sorteados.filter(p => p !== sorteado);
        }

        alert("Sorteio realizado com sucesso!");
        return true;
    }

    consultarAmigoSecreto(nome) {
        nome = nome.trim();
        if (!this.sorteio.size) {
            alert("O sorteio ainda não foi realizado!");
            return null;
        }
        if (!this.sorteio.has(nome)) {
            alert("Nome não encontrado!");
            return null;
        }
        return this.sorteio.get(nome);
    }
}

// Instância global
const app = new AmigoSecreto();

// Funções da interface
function adicionarParticipante() {
    const input = document.getElementById('nomeParticipante');
    const nome = input.value;

    if (app.adicionarParticipante(nome)) {
        atualizarListaParticipantes();
        input.value = ''; // Limpar input
    }
}

function atualizarListaParticipantes() {
    const lista = document.getElementById('listaParticipantes');
    lista.innerHTML = app.participantes
        .map(nome => `<div>${nome}</div>`)
        .join('');
}

function realizarSorteio() {
    app.realizarSorteio();
}

function verAmigoSecreto() {
    const nome = prompt("Digite seu nome:");
    if (!nome) return;

    const amigoSecreto = app.consultarAmigoSecreto(nome);
    if (amigoSecreto) {
        alert(`Olá ${nome}!\nSeu amigo secreto é: ${amigoSecreto}`);
    }
}
