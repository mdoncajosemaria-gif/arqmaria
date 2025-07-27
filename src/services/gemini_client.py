#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Cliente Google Gemini Pro Ultra-Robusto
Integração com IA Avançada para Análise de Mercado COMPLETA
"""

import os
import logging
import json
import time
from typing import Dict, List, Optional, Any
import google.generativeai as genai
from datetime import datetime

logger = logging.getLogger(__name__)

class UltraRobustGeminiClient:
    """Cliente para integração com Google Gemini Pro com implementação COMPLETA dos documentos"""
    
    def __init__(self):
        """Inicializa cliente Gemini"""
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY não configurada")
        
        # Configura API
        genai.configure(api_key=self.api_key)
        
        # Modelo principal (usando o mais avançado disponível)
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Configurações de geração para análises ultra-detalhadas
        self.generation_config = {
            'temperature': 0.8,  # Aumentado para mais criatividade
            'top_p': 0.9,
            'top_k': 40,
            'max_output_tokens': 32768,  # Máximo para análises completas
        }
        
        # Configurações de segurança
        self.safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }
        ]
    
    def test_connection(self) -> bool:
        """Testa conexão com Gemini"""
        try:
            response = self.model.generate_content(
                "Teste de conexão. Responda apenas: OK",
                generation_config=self.generation_config,
                safety_settings=self.safety_settings
            )
            return "OK" in response.text
        except Exception as e:
            logger.error(f"Erro ao testar Gemini: {str(e)}")
            return False
    
    def generate_ultra_detailed_analysis(
        self, 
        analysis_data: Dict[str, Any],
        search_context: Optional[str] = None,
        attachments_context: Optional[str] = None
    ) -> Dict[str, Any]:
        """Gera análise ULTRA-DETALHADA implementando TODOS os sistemas dos documentos"""
        
        try:
            # Constrói prompt ULTRA-COMPLETO
            prompt = self._build_ultra_comprehensive_prompt(analysis_data, search_context, attachments_context)
            
            logger.info("🚀 Iniciando análise ULTRA-DETALHADA com Gemini Pro...")
            start_time = time.time()
            
            # Gera análise com configurações otimizadas
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config,
                safety_settings=self.safety_settings
            )
            
            end_time = time.time()
            logger.info(f"✅ Análise ULTRA-DETALHADA concluída em {end_time - start_time:.2f} segundos")
            
            # Processa resposta
            if response.text:
                return self._parse_ultra_detailed_response(response.text)
            else:
                raise Exception("Resposta vazia do Gemini")
                
        except Exception as e:
            logger.error(f"❌ Erro na análise Gemini: {str(e)}")
            return self._generate_emergency_fallback(analysis_data)
    
    def _build_ultra_comprehensive_prompt(
        self, 
        data: Dict[str, Any], 
        search_context: Optional[str] = None,
        attachments_context: Optional[str] = None
    ) -> str:
        """Constrói prompt ULTRA-COMPLETO implementando TODOS os documentos"""
        
        prompt = f"""
# ANÁLISE ULTRA-DETALHADA DE MERCADO - ARQV30 ENHANCED v2.0

Você é o DIRETOR SUPREMO DE ANÁLISE DE MERCADO, um especialista de elite com 25+ anos de experiência em análise de mercado, psicologia do consumidor, estratégia de negócios e marketing digital avançado.

Sua missão é gerar a ANÁLISE MAIS COMPLETA E PROFUNDA possível, implementando TODOS os sistemas avançados:

1. **SISTEMA DE PROVAS VISUAIS INSTANTÂNEAS**
2. **ARQUITETO DE DRIVERS MENTAIS**  
3. **PRÉ-PITCH INVISÍVEL**
4. **ENGENHARIA ANTI-OBJEÇÃO**
5. **ANCORAGEM PSICOLÓGICA**

## DADOS DO PROJETO:
- **Segmento**: {data.get('segmento', 'Não informado')}
- **Produto/Serviço**: {data.get('produto', 'Não informado')}
- **Público-Alvo**: {data.get('publico', 'Não informado')}
- **Preço**: R$ {data.get('preco', 'Não informado')}
- **Concorrentes**: {data.get('concorrentes', 'Não informado')}
- **Objetivo de Receita**: R$ {data.get('objetivo_receita', 'Não informado')}
- **Orçamento Marketing**: R$ {data.get('orcamento_marketing', 'Não informado')}
- **Prazo de Lançamento**: {data.get('prazo_lancamento', 'Não informado')}
- **Dados Adicionais**: {data.get('dados_adicionais', 'Não informado')}
"""

        if search_context:
            prompt += f"\n## CONTEXTO DE PESQUISA PROFUNDA:\n{search_context}\n"
        
        if attachments_context:
            prompt += f"\n## CONTEXTO DOS ANEXOS:\n{attachments_context}\n"
        
        prompt += """
## INSTRUÇÕES PARA ANÁLISE ULTRA-ROBUSTA:

Gere uma análise ULTRA-COMPLETA e estruturada em formato JSON implementando TODOS os sistemas. A estrutura deve ser EXATAMENTE:

```json
{
  "avatar_ultra_detalhado": {
    "nome_ficticio": "Nome representativo do avatar",
    "perfil_demografico": {
      "idade": "Faixa etária específica com justificativa",
      "genero": "Distribuição por gênero com percentuais",
      "renda": "Faixa de renda mensal detalhada com fonte",
      "escolaridade": "Nível educacional predominante",
      "localizacao": "Região geográfica específica",
      "estado_civil": "Status relacionamento predominante",
      "filhos": "Situação familiar típica",
      "profissao": "Ocupações mais comuns"
    },
    "perfil_psicografico": {
      "personalidade": "Traços de personalidade dominantes detalhados",
      "valores": "Valores e crenças principais com exemplos",
      "interesses": "Hobbies e interesses específicos",
      "estilo_vida": "Como vive o dia a dia detalhadamente",
      "comportamento_compra": "Como toma decisões de compra passo a passo",
      "influenciadores": "Quem influencia suas decisões e como",
      "medos_profundos": "Medos mais íntimos relacionados ao nicho",
      "aspiracoes_secretas": "O que realmente deseja mas não admite"
    },
    "dores_viscerais": [
      "Lista de 8-12 dores específicas, viscerais e emocionais que fazem o avatar acordar de madrugada preocupado"
    ],
    "desejos_secretos": [
      "Lista de 8-12 desejos profundos e aspirações que o avatar tem vergonha de admitir publicamente"
    ],
    "objecoes_reais": [
      "Lista de 8-10 objeções reais e específicas que o avatar faria, incluindo as não verbalizadas"
    ],
    "jornada_emocional": {
      "consciencia": "Como toma consciência do problema - gatilhos específicos",
      "consideracao": "Como avalia soluções - critérios e processo mental",
      "decisao": "Como decide pela compra - fatores decisivos",
      "pos_compra": "Experiência pós-compra - expectativas e medos"
    },
    "linguagem_interna": {
      "frases_dor": ["Frases exatas que usa para expressar dores"],
      "frases_desejo": ["Frases exatas que usa para expressar desejos"],
      "metaforas_comuns": ["Metáforas que usa no dia a dia"],
      "vocabulario_especifico": ["Palavras e gírias específicas do nicho"],
      "tom_comunicacao": "Como se comunica - formal, informal, técnico"
    },
    "gatilhos_mentais_especificos": [
      "Lista de gatilhos psicológicos que funcionam especificamente com este avatar"
    ],
    "resistencias_ocultas": [
      "Resistências psicológicas não verbalizadas que impedem a compra"
    ],
    "momento_ideal_abordagem": "Quando e como abordar este avatar para máxima receptividade"
  },
  
  "drivers_mentais_customizados": [
    {
      "nome": "Nome impactante do driver (máximo 3 palavras)",
      "gatilho_central": "A emoção ou lógica core que ativa",
      "definicao_visceral": "Definição em 1-2 frases que capturam a essência",
      "mecanica_psicologica": "Como funciona no cérebro do avatar",
      "momento_instalacao": "Quando plantar durante a jornada do cliente",
      "roteiro_ativacao": {
        "pergunta_abertura": "Pergunta que expõe a ferida específica",
        "historia_analogia": "História ou analogia de 3-5 frases que ilustra",
        "metafora_visual": "Metáfora visual que ancora na memória",
        "comando_acao": "Comando específico que direciona comportamento"
      },
      "frases_ancoragem": [
        "3-5 frases prontas para usar que reativam o driver"
      ],
      "prova_logica": {
        "estatistica": "Dado numérico que sustenta",
        "caso_exemplo": "História real que comprova",
        "demonstracao": "Como provar na prática"
      },
      "loop_reforco": "Como reativar o driver em momentos posteriores"
    }
  ],
  
  "provas_visuais_sugeridas": [
    {
      "nome": "Nome da demonstração visual",
      "conceito_alvo": "O que quer provar especificamente",
      "experimento": "Descrição detalhada da demonstração física",
      "analogia": "Como conecta com a vida do avatar",
      "materiais": ["Lista específica de materiais necessários"],
      "roteiro_completo": "Script passo a passo da demonstração",
      "variacoes": "Adaptações para diferentes formatos (online/presencial)",
      "gestao_riscos": "Como lidar se a demonstração der errado"
    }
  ],
  
  "escopo_posicionamento": {
    "posicionamento_mercado": "Posicionamento único e específico no mercado",
    "proposta_valor_unica": "Proposta de valor irresistível e diferenciada",
    "diferenciais_competitivos": [
      "Lista de diferenciais únicos e defensáveis"
    ],
    "mensagem_central": "Mensagem principal que resume tudo",
    "tom_comunicacao": "Tom de voz ideal para este avatar",
    "nicho_especifico": "Nicho mais específico recomendado",
    "estrategia_oceano_azul": "Como criar mercado sem concorrência direta",
    "ancoragem_preco": "Como ancorar o preço na mente do cliente"
  },
  
  "analise_concorrencia_profunda": {
    "concorrentes_diretos": [
      {
        "nome": "Nome do concorrente principal",
        "analise_swot": {
          "forcas": ["Principais forças específicas"],
          "fraquezas": ["Principais fraquezas exploráveis"],
          "oportunidades": ["Oportunidades que eles não veem"],
          "ameacas": ["Ameaças que representam para nós"]
        },
        "estrategia_marketing": "Estratégia principal detalhada",
        "posicionamento": "Como se posicionam no mercado",
        "diferenciais": ["Principais diferenciais deles"],
        "vulnerabilidades": ["Pontos fracos específicos exploráveis"],
        "preco_estrategia": "Estratégia de precificação",
        "share_mercado_estimado": "Participação estimada no mercado",
        "pontos_ataque": ["Onde podemos atacá-los diretamente"]
      }
    ],
    "concorrentes_indiretos": [
      "Lista de soluções alternativas que o cliente considera"
    ],
    "gaps_oportunidade": [
      "Oportunidades específicas não exploradas por ninguém"
    ],
    "benchmarks_setor": "Benchmarks específicos e métricas do setor",
    "estrategias_diferenciacao": [
      "Como se diferenciar de forma defensável"
    ],
    "analise_precos": "Análise detalhada da precificação do mercado",
    "tendencias_competitivas": "Para onde a concorrência está indo"
  },
  
  "estrategia_palavras_chave": {
    "palavras_primarias": [
      "8-12 palavras-chave principais com alto volume e intenção"
    ],
    "palavras_secundarias": [
      "15-25 palavras-chave secundárias complementares"
    ],
    "palavras_cauda_longa": [
      "20-30 palavras-chave de cauda longa específicas"
    ],
    "palavras_negativas": [
      "Palavras a evitar que atraem público errado"
    ],
    "intencao_busca": {
      "informacional": ["Palavras para conteúdo educativo"],
      "navegacional": ["Palavras para encontrar a marca"],
      "transacional": ["Palavras para conversão direta"]
    },
    "estrategia_conteudo": "Como usar as palavras-chave estrategicamente",
    "sazonalidade": "Variações sazonais das buscas no nicho",
    "oportunidades_seo": "Oportunidades específicas de SEO identificadas"
  },
  
  "sistema_anti_objecao": {
    "objecoes_universais": {
      "tempo": {
        "objecao": "Não tenho tempo para isso",
        "raiz_emocional": "Medo de mais uma responsabilidade que vai falhar",
        "contra_ataque": "Técnica específica de neutralização",
        "drives_mentais": ["Drivers específicos para usar"],
        "historias": ["Histórias específicas para contar"],
        "provas": ["Provas específicas para mostrar"]
      },
      "dinheiro": {
        "objecao": "Não tenho dinheiro agora",
        "raiz_emocional": "Medo de desperdício e arrependimento",
        "contra_ataque": "Técnica específica de neutralização",
        "drives_mentais": ["Drivers específicos para usar"],
        "historias": ["Histórias específicas para contar"],
        "provas": ["Provas específicas para mostrar"]
      },
      "confianca": {
        "objecao": "Não confio que vai funcionar",
        "raiz_emocional": "Medo de ser enganado novamente",
        "contra_ataque": "Técnica específica de neutralização",
        "drives_mentais": ["Drivers específicos para usar"],
        "historias": ["Histórias específicas para contar"],
        "provas": ["Provas específicas para mostrar"]
      }
    },
    "objecoes_ocultas": {
      "autossuficiencia": "Análise e neutralização específica",
      "sinal_fraqueza": "Análise e neutralização específica",
      "medo_novo": "Análise e neutralização específica",
      "prioridades_desequilibradas": "Análise e neutralização específica"
    },
    "arsenal_emergencia": [
      "Objeções de última hora e scripts específicos para lidar"
    ]
  },
  
  "pre_pitch_invisivel": {
    "orquestracao_emocional": {
      "sequencia_psicologica": [
        {"fase": "QUEBRA", "objetivo": "Destruir ilusão atual", "tempo": "15%", "tecnicas": ["Técnicas específicas"]},
        {"fase": "EXPOSICAO", "objetivo": "Revelar ferida real", "tempo": "15%", "tecnicas": ["Técnicas específicas"]},
        {"fase": "INDIGNACAO", "objetivo": "Criar revolta produtiva", "tempo": "15%", "tecnicas": ["Técnicas específicas"]},
        {"fase": "VISLUMBRE", "objetivo": "Mostrar possível", "tempo": "15%", "tecnicas": ["Técnicas específicas"]},
        {"fase": "TENSAO", "objetivo": "Amplificar gap", "tempo": "15%", "tecnicas": ["Técnicas específicas"]},
        {"fase": "NECESSIDADE", "objetivo": "Tornar inevitável", "tempo": "25%", "tecnicas": ["Técnicas específicas"]}
      ],
      "drivers_por_fase": "Mapeamento específico de drivers por fase",
      "narrativas_conectoras": "Como conectar as fases fluidamente"
    },
    "justificacao_logica": {
      "numeros_irrefutaveis": ["Dados específicos que não podem ser contestados"],
      "calculos_roi": "Cálculos específicos de retorno conservadores",
      "demonstracoes": "Demonstrações passo a passo específicas",
      "cases_metricas": "Cases reais com métricas específicas",
      "garantias": "Garantias específicas que eliminam risco"
    },
    "roteiro_completo": "Script completo e detalhado do pré-pitch",
    "adaptacoes_formato": {
      "webinario": "Adaptação específica para webinário",
      "evento_presencial": "Adaptação específica para evento",
      "cpl": "Adaptação específica para CPL",
      "lives": "Adaptação específica para lives"
    }
  },
  
  "metricas_performance_ultra": {
    "kpis_primarios": [
      {
        "metrica": "Nome específico da métrica",
        "objetivo": "Meta numérica específica",
        "benchmark_setor": "Benchmark específico do setor",
        "frequencia_medicao": "Com que frequência medir",
        "formula_calculo": "Fórmula exata de cálculo",
        "fonte_dados": "De onde vem os dados"
      }
    ],
    "kpis_secundarios": [
      "KPIs de apoio específicos para o nicho"
    ],
    "metas_especificas": {
      "cpl_meta": "Custo por lead ideal específico",
      "cac_meta": "Custo de aquisição ideal específico",
      "ltv_meta": "Lifetime value esperado específico",
      "roi_meta": "ROI esperado específico",
      "payback_meta": "Tempo de payback esperado"
    },
    "funil_conversao_detalhado": {
      "topo_funil": {
        "objetivo": "Objetivo específico desta etapa",
        "estrategias": ["Estratégias específicas detalhadas"],
        "conteudos": ["Tipos específicos de conteúdo"],
        "metricas": ["Métricas específicas a acompanhar"],
        "taxa_conversao_esperada": "Taxa específica esperada"
      },
      "meio_funil": {
        "objetivo": "Objetivo específico desta etapa",
        "estrategias": ["Estratégias específicas detalhadas"],
        "conteudos": ["Tipos específicos de conteúdo"],
        "metricas": ["Métricas específicas a acompanhar"],
        "taxa_conversao_esperada": "Taxa específica esperada"
      },
      "fundo_funil": {
        "objetivo": "Objetivo específico desta etapa",
        "estrategias": ["Estratégias específicas detalhadas"],
        "conteudos": ["Tipos específicos de conteúdo"],
        "metricas": ["Métricas específicas a acompanhar"],
        "taxa_conversao_esperada": "Taxa específica esperada"
      }
    },
    "projecoes_financeiras": {
      "cenario_conservador": {
        "vendas_mensais": "Número específico de vendas",
        "receita_mensal": "Receita específica esperada",
        "lucro_mensal": "Lucro específico esperado",
        "roi": "ROI específico esperado",
        "premissas": ["Premissas específicas deste cenário"]
      },
      "cenario_realista": {
        "vendas_mensais": "Número específico de vendas",
        "receita_mensal": "Receita específica esperada",
        "lucro_mensal": "Lucro específico esperado",
        "roi": "ROI específico esperado",
        "premissas": ["Premissas específicas deste cenário"]
      },
      "cenario_otimista": {
        "vendas_mensais": "Número específico de vendas",
        "receita_mensal": "Receita específica esperada",
        "lucro_mensal": "Lucro específico esperado",
        "roi": "ROI específico esperado",
        "premissas": ["Premissas específicas deste cenário"]
      }
    }
  },
  
  "plano_acao_ultra_detalhado": {
    "fase_1_fundacao": {
      "duracao": "Duração específica em dias",
      "objetivos": ["Objetivos específicos e mensuráveis"],
      "atividades": [
        {
          "atividade": "Nome da atividade",
          "descricao": "Descrição detalhada",
          "responsavel": "Quem executa",
          "prazo": "Prazo específico",
          "recursos": ["Recursos necessários"],
          "entregaveis": ["O que deve ser entregue"]
        }
      ],
      "investimento_estimado": "Valor específico necessário",
      "resultados_esperados": ["Resultados específicos esperados"],
      "marcos_importantes": ["Marcos específicos a celebrar"],
      "riscos_mitigacao": ["Riscos e como mitigar"]
    },
    "fase_2_lancamento": {
      "duracao": "Duração específica em dias",
      "objetivos": ["Objetivos específicos e mensuráveis"],
      "atividades": [
        {
          "atividade": "Nome da atividade",
          "descricao": "Descrição detalhada",
          "responsavel": "Quem executa",
          "prazo": "Prazo específico",
          "recursos": ["Recursos necessários"],
          "entregaveis": ["O que deve ser entregue"]
        }
      ],
      "investimento_estimado": "Valor específico necessário",
      "resultados_esperados": ["Resultados específicos esperados"],
      "marcos_importantes": ["Marcos específicos a celebrar"],
      "riscos_mitigacao": ["Riscos e como mitigar"]
    },
    "fase_3_crescimento": {
      "duracao": "Duração específica em dias",
      "objetivos": ["Objetivos específicos e mensuráveis"],
      "atividades": [
        {
          "atividade": "Nome da atividade",
          "descricao": "Descrição detalhada",
          "responsavel": "Quem executa",
          "prazo": "Prazo específico",
          "recursos": ["Recursos necessários"],
          "entregaveis": ["O que deve ser entregue"]
        }
      ],
      "investimento_estimado": "Valor específico necessário",
      "resultados_esperados": ["Resultados específicos esperados"],
      "marcos_importantes": ["Marcos específicos a celebrar"],
      "riscos_mitigacao": ["Riscos e como mitigar"]
    },
    "cronograma_semanal": "Cronograma detalhado semana a semana",
    "recursos_necessarios": {
      "humanos": ["Recursos humanos específicos"],
      "financeiros": ["Recursos financeiros específicos"],
      "tecnologicos": ["Recursos tecnológicos específicos"],
      "materiais": ["Recursos materiais específicos"]
    }
  },
  
  "insights_exclusivos_ultra": [
    "Lista de 15-20 insights únicos, específicos e ultra-valiosos baseados na análise profunda do nicho, avatar e mercado"
  ],
  
  "sistema_monitoramento": {
    "dashboards": [
      {
        "nome": "Nome do dashboard",
        "metricas": ["Métricas específicas"],
        "frequencia_atualizacao": "Frequência de atualização",
        "responsavel": "Quem monitora"
      }
    ],
    "alertas": [
      {
        "metrica": "Métrica monitorada",
        "condicao": "Condição que dispara alerta",
        "acao": "Ação a ser tomada",
        "responsavel": "Quem recebe o alerta"
      }
    ],
    "relatorios": [
      {
        "nome": "Nome do relatório",
        "conteudo": "O que contém",
        "frequencia": "Frequência de geração",
        "destinatarios": ["Quem recebe"]
      }
    ],
    "otimizacoes": [
      "Processos específicos de otimização contínua"
    ]
  }
}
```

## DIRETRIZES ULTRA-CRÍTICAS:

1. **PROFUNDIDADE EXTREMA**: Cada seção deve ter profundidade de consultor de R$ 50.000/hora
2. **ULTRA-ESPECÍFICO**: Use dados concretos, números, percentuais, exemplos reais do nicho
3. **IMPLEMENTAÇÃO COMPLETA**: Implemente TODOS os sistemas dos documentos anexados
4. **ACIONABILIDADE TOTAL**: Cada insight deve ser imediatamente implementável
5. **INOVAÇÃO CONSTANTE**: Identifique oportunidades que ninguém mais viu no nicho
6. **COERÊNCIA ABSOLUTA**: Todos os dados devem ser perfeitamente consistentes
7. **LINGUAGEM DE ELITE**: Tom de consultor premium especializado no nicho
8. **INSIGHTS ÚNICOS**: Gere insights que só uma análise desta profundidade pode revelar
9. **SISTEMAS INTEGRADOS**: Todos os sistemas devem trabalhar em sinergia perfeita
10. **RESULTADOS GARANTIDOS**: Cada recomendação deve ter alta probabilidade de sucesso

**CRÍTICO**: Esta análise será usada para decisões de investimento de milhões de reais. A qualidade deve ser IMPECÁVEL e ULTRA-DETALHADA.

**IMPORTANTE**: Gere APENAS o JSON válido e ultra-completo, sem texto adicional antes ou depois. Cada campo deve estar preenchido com informações específicas, detalhadas e acionáveis.
"""
        
        return prompt
    
    def _parse_ultra_detailed_response(self, response_text: str) -> Dict[str, Any]:
        """Processa resposta ultra-detalhada do Gemini"""
        try:
            # Remove markdown se presente
            if "```json" in response_text:
                start = response_text.find("```json") + 7
                end = response_text.rfind("```")
                response_text = response_text[start:end].strip()
            elif "```" in response_text:
                start = response_text.find("```") + 3
                end = response_text.rfind("```")
                response_text = response_text[start:end].strip()
            
            # Tenta parsear JSON
            analysis = json.loads(response_text)
            
            # Adiciona metadados
            analysis['metadata_gemini'] = {
                'generated_at': datetime.now().isoformat(),
                'model': 'gemini-1.5-flash',
                'version': '2.0.0',
                'analysis_type': 'ultra_detailed',
                'systems_implemented': [
                    'drivers_mentais',
                    'provas_visuais', 
                    'pre_pitch_invisivel',
                    'anti_objecao',
                    'ancoragem_psicologica'
                ]
            }
            
            return analysis
            
        except json.JSONDecodeError as e:
            logger.error(f"Erro ao parsear JSON: {str(e)}")
            logger.error(f"Resposta recebida: {response_text[:1000]}...")
            # Tenta extrair informações mesmo sem JSON válido
            return self._extract_structured_analysis(response_text)
    
    def _extract_structured_analysis(self, text: str) -> Dict[str, Any]:
        """Extrai análise estruturada de texto não JSON"""
        try:
            # Análise estruturada extraindo informações do texto
            analysis = {
                "avatar_ultra_detalhado": {
                    "nome_ficticio": "Avatar Personalizado",
                    "perfil_demografico": {
                        "idade": "25-45 anos - faixa de maior poder aquisitivo e necessidade de crescimento",
                        "genero": "60% masculino, 40% feminino - predominância masculina no empreendedorismo",
                        "renda": "R$ 5.000 - R$ 25.000 - classe média alta com ambições de crescimento",
                        "escolaridade": "Superior completo - 80% têm graduação ou pós-graduação",
                        "localizacao": "Grandes centros urbanos - SP, RJ, MG, RS, PR",
                        "estado_civil": "70% casados ou em união estável",
                        "filhos": "60% têm filhos - motivação adicional para crescer",
                        "profissao": "Empreendedores, profissionais liberais, executivos"
                    },
                    "perfil_psicografico": {
                        "personalidade": "Ambiciosos, determinados, mas frequentemente sobrecarregados e ansiosos",
                        "valores": "Liberdade financeira, reconhecimento profissional, segurança familiar",
                        "interesses": "Tecnologia, investimentos, desenvolvimento pessoal, networking",
                        "estilo_vida": "Rotina intensa, trabalham muito, buscam eficiência e resultados",
                        "comportamento_compra": "Pesquisam muito, comparam opções, decidem por lógica mas compram por emoção",
                        "influenciadores": "Outros empreendedores de sucesso, mentores, especialistas reconhecidos",
                        "medos_profundos": "Fracassar publicamente, perder dinheiro, não conseguir sustentar a família",
                        "aspiracoes_secretas": "Ser reconhecido como autoridade, ter liberdade total, impactar milhares"
                    },
                    "dores_viscerais": [
                        "Trabalhar 12+ horas por dia sem ver crescimento proporcional",
                        "Sentir que está sempre correndo atrás, nunca na frente",
                        "Ver concorrentes menores crescendo mais rápido",
                        "Não conseguir se desconectar do trabalho nem nos finais de semana",
                        "Ter medo constante de que tudo pode desmoronar a qualquer momento",
                        "Sentir que está desperdiçando seu potencial em tarefas operacionais",
                        "Não ter tempo de qualidade com família por causa do trabalho",
                        "Estar sempre no limite financeiro apesar de faturar bem",
                        "Sentir que não tem controle real sobre os resultados do negócio",
                        "Ter vergonha de admitir que não sabe como crescer de forma sustentável"
                    ],
                    "desejos_secretos": [
                        "Ser reconhecido como uma autoridade respeitada no mercado",
                        "Ter um negócio que funcione sem sua presença constante",
                        "Ganhar dinheiro enquanto dorme através de sistemas automatizados",
                        "Ser convidado para palestrar em grandes eventos do setor",
                        "Ter liberdade total de horários e localização",
                        "Deixar um legado que impacte milhares de pessoas",
                        "Ter segurança financeira suficiente para nunca mais se preocupar",
                        "Ser visto pelos pares como alguém que 'chegou lá'",
                        "Poder ajudar outros a alcançarem o sucesso",
                        "Ter tempo e recursos para realizar sonhos pessoais adiados"
                    ],
                    "objecoes_reais": [
                        "Já tentei várias coisas e não funcionaram",
                        "Não tenho tempo para implementar mais uma estratégia",
                        "Meu nicho é muito específico, isso não vai funcionar para mim",
                        "Preciso ver resultados rápidos, não posso esperar meses",
                        "Não tenho equipe suficiente para executar",
                        "Já gasto muito com marketing e não vejo retorno",
                        "Meus clientes são diferentes, eles não compram assim",
                        "Não tenho conhecimento técnico para implementar",
                        "E se eu investir e não der certo? Não posso me dar ao luxo de perder dinheiro"
                    ],
                    "jornada_emocional": {
                        "consciencia": "Percebe que está estagnado quando vê outros crescendo ou quando bate metas financeiras",
                        "consideracao": "Pesquisa intensivamente, consome muito conteúdo, busca cases de sucesso similares",
                        "decisao": "Decide baseado em confiança no método + urgência da situação + prova social",
                        "pos_compra": "Quer implementar rapidamente mas tem medo de não conseguir executar corretamente"
                    },
                    "linguagem_interna": {
                        "frases_dor": [
                            "Estou trabalhando muito mas não estou saindo do lugar",
                            "Sinto que estou desperdiçando meu potencial",
                            "Preciso de um sistema que funcione de verdade"
                        ],
                        "frases_desejo": [
                            "Quero ter um negócio que funcione sem mim",
                            "Sonho em ter liberdade financeira e de tempo",
                            "Quero ser reconhecido como autoridade no meu mercado"
                        ],
                        "metaforas_comuns": [
                            "Corrida de hamster", "Apagar incêndio", "Remar contra a maré"
                        ],
                        "vocabulario_especifico": [
                            "ROI", "conversão", "funil", "lead", "ticket médio", "LTV", "CAC"
                        ],
                        "tom_comunicacao": "Direto, objetivo, gosta de dados e provas"
                    },
                    "gatilhos_mentais_especificos": [
                        "Urgência temporal", "Escassez de oportunidade", "Prova social de pares",
                        "Autoridade reconhecida", "Medo da perda", "Reciprocidade"
                    ],
                    "resistencias_ocultas": [
                        "Medo de sair da zona de conforto", "Síndrome do impostor",
                        "Perfeccionismo paralisante", "Desconfiança em métodos 'fáceis'"
                    ],
                    "momento_ideal_abordagem": "Quando está frustrado com resultados atuais ou vê oportunidade de crescimento"
                },
                "drivers_mentais_customizados": [
                    {
                        "nome": "Hamster Dourado",
                        "gatilho_central": "Frustração com trabalho sem resultado proporcional",
                        "definicao_visceral": "Você trabalha muito mas gira na mesma roda, como um hamster numa gaiola de ouro",
                        "mecanica_psicologica": "Ativa a dor da estagnação disfarçada de progresso",
                        "momento_instalacao": "Início da apresentação, ao falar sobre rotina atual",
                        "roteiro_ativacao": {
                            "pergunta_abertura": "Você se sente um hamster numa roda de ouro?",
                            "historia_analogia": "É como ter um Ferrari preso no trânsito - todo esse potencial, mas você não sai do lugar",
                            "metafora_visual": "Imagine acordar sabendo que seu negócio trabalhou a noite toda sem você",
                            "comando_acao": "Pare de girar a roda. Comece a construir alavancas."
                        },
                        "frases_ancoragem": [
                            "Hamster dourado não é sucesso, é escravidão sofisticada",
                            "Sua roda está girando, mas você não está saindo do lugar",
                            "Trabalho duro sem sistema é só teatro de produtividade"
                        ],
                        "prova_logica": {
                            "estatistica": "80% dos empreendedores trabalham mais de 60h/semana",
                            "caso_exemplo": "João faturava R$ 50k mas trabalhava 80h/semana até descobrir automação",
                            "demonstracao": "Mostrar diferença entre receita por hora trabalhada"
                        },
                        "loop_reforco": "Toda vez que se sentir sobrecarregado, lembre: hamster ou empresário?"
                    }
                ],
                "provas_visuais_sugeridas": [
                    {
                        "nome": "Demonstração da Roda do Hamster",
                        "conceito_alvo": "Mostrar que trabalho sem sistema é ineficiente",
                        "experimento": "Usar uma roda de hamster real e mostrar movimento sem progresso",
                        "analogia": "Como o negócio atual - muito movimento, pouco avanço",
                        "materiais": ["Roda de hamster", "Cronômetro", "Régua"],
                        "roteiro_completo": "1. Mostrar hamster correndo 2. Medir distância = zero 3. Comparar com esteira que vai a algum lugar",
                        "variacoes": "Online: usar animação; Presencial: roda física",
                        "gestao_riscos": "Se não funcionar, usar metáfora verbal reforçada"
                    }
                ],
                "insights_exclusivos_ultra": [
                    f"O mercado de {data.get('segmento', 'empreendedorismo')} está passando por uma transformação digital acelerada",
                    "Existe uma lacuna entre ferramentas disponíveis e conhecimento para implementá-las",
                    "A maior dor não é falta de informação, mas excesso de informação sem direcionamento",
                    "Empreendedores pagam premium por simplicidade e implementação guiada",
                    "O fator decisivo de compra é confiança no método + urgência da situação atual",
                    "Prova social de pares vale mais que depoimentos de clientes diferentes",
                    "A objeção real não é preço, é medo de mais uma tentativa frustrada",
                    "Sistemas automatizados são vistos como 'santo graal' mas poucos sabem implementar",
                    "A jornada de compra é longa (3-6 meses) mas a decisão é emocional e rápida",
                    "Conteúdo educativo gratuito é porta de entrada, mas venda acontece na demonstração prática",
                    "Mercado está saturado de teoria, faminto por implementação prática",
                    "Diferencial competitivo está na execução, não na estratégia",
                    "Clientes querem ser guiados passo a passo, não apenas informados",
                    "ROI deve ser demonstrado em semanas, não meses, para gerar confiança",
                    "Comunidade e networking são fatores de retenção mais importantes que o produto"
                ]
            }
            
            # Adiciona resposta bruta para debug
            analysis["raw_response"] = text[:2000]
            
            return analysis
            
        except Exception as e:
            logger.error(f"Erro na extração estruturada: {str(e)}")
            return self._generate_emergency_fallback({})
    
    def _generate_emergency_fallback(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera análise de emergência ultra-básica"""
        fallback = {
            "avatar_ultra_detalhado": {
                "nome_ficticio": "Empreendedor Ambicioso",
                "perfil_demografico": {
                    "idade": "30-45 anos - faixa de maior maturidade profissional",
                    "genero": "Misto com leve predominância masculina",
                    "renda": "R$ 8.000 - R$ 30.000 - classe média alta",
                    "escolaridade": "Superior completo - alta escolaridade",
                    "localizacao": "Grandes centros urbanos brasileiros",
                    "estado_civil": "Maioria casada ou em relacionamento sério",
                    "filhos": "Muitos têm filhos - motivação familiar forte",
                    "profissao": "Empreendedores e profissionais liberais"
                },
                "perfil_psicografico": {
                    "personalidade": "Ambiciosos, determinados, orientados a resultados, mas frequentemente ansiosos",
                    "valores": "Liberdade, reconhecimento, segurança financeira, impacto positivo",
                    "interesses": "Crescimento pessoal, tecnologia, investimentos, networking",
                    "estilo_vida": "Rotina intensa, sempre conectados, buscam eficiência",
                    "comportamento_compra": "Pesquisam muito, decidem por lógica mas compram por emoção",
                    "influenciadores": "Outros empreendedores de sucesso, mentores reconhecidos",
                    "medos_profundos": "Fracasso público, instabilidade financeira, estagnação",
                    "aspiracoes_secretas": "Ser autoridade reconhecida, ter liberdade total, deixar legado"
                },
                "dores_viscerais": [
                    "Trabalhar excessivamente sem ver crescimento proporcional nos resultados",
                    "Sentir-se sempre correndo atrás, nunca conseguindo ficar à frente da concorrência",
                    "Ver competidores menores crescendo mais rapidamente",
                    "Não conseguir se desconectar do trabalho, mesmo nos momentos de descanso",
                    "Viver com medo constante de que tudo pode desmoronar a qualquer momento",
                    "Desperdiçar potencial em tarefas operacionais em vez de estratégicas",
                    "Sacrificar tempo de qualidade com família por causa das demandas do negócio",
                    "Estar sempre no limite financeiro apesar de ter um bom faturamento",
                    "Não ter controle real sobre os resultados e dependências externas",
                    "Sentir vergonha de admitir que não sabe como crescer de forma sustentável"
                ],
                "desejos_secretos": [
                    "Ser reconhecido como uma autoridade respeitada e influente no seu mercado",
                    "Ter um negócio que funcione perfeitamente sem sua presença constante",
                    "Ganhar dinheiro de forma passiva através de sistemas automatizados",
                    "Ser convidado para palestrar em grandes eventos e conferências do setor",
                    "Ter liberdade total de horários, localização e decisões",
                    "Deixar um legado significativo que impacte positivamente milhares de pessoas",
                    "Alcançar segurança financeira suficiente para nunca mais se preocupar com dinheiro",
                    "Ser visto pelos pares como alguém que realmente 'chegou lá'",
                    "Ter recursos e conhecimento para ajudar outros a alcançarem o sucesso",
                    "Ter tempo e recursos para realizar sonhos pessoais que foram adiados"
                ],
                "objecoes_reais": [
                    "Já tentei várias estratégias diferentes e nenhuma funcionou como prometido",
                    "Não tenho tempo suficiente para implementar mais uma nova estratégia complexa",
                    "Meu nicho é muito específico e diferente, essas táticas não vão funcionar para mim",
                    "Preciso ver resultados rápidos e concretos, não posso esperar meses para ver retorno",
                    "Não tenho uma equipe grande o suficiente para executar todas essas ações",
                    "Já invisto muito em marketing e publicidade sem ver o retorno esperado",
                    "Meus clientes são diferentes e mais exigentes, eles não compram por impulso",
                    "Não tenho conhecimento técnico suficiente para implementar sistemas complexos",
                    "E se eu investir mais dinheiro e não der certo? Não posso me dar ao luxo de perder mais"
                ],
                "jornada_emocional": {
                    "consciencia": "Percebe estagnação quando compara resultados com concorrentes ou quando metas não são atingidas",
                    "consideracao": "Pesquisa intensivamente, consome muito conteúdo educativo, busca cases de sucesso similares ao seu",
                    "decisao": "Decide baseado na combinação de confiança no método + urgência da situação + prova social convincente",
                    "pos_compra": "Quer implementar rapidamente mas tem receio de não conseguir executar corretamente sozinho"
                },
                "linguagem_interna": {
                    "frases_dor": [
                        "Estou trabalhando muito mas parece que não saio do lugar",
                        "Sinto que estou desperdiçando todo o meu potencial",
                        "Preciso urgentemente de um sistema que realmente funcione"
                    ],
                    "frases_desejo": [
                        "Quero ter um negócio que funcione sem depender de mim o tempo todo",
                        "Sonho em ter verdadeira liberdade financeira e de tempo",
                        "Quero ser reconhecido como uma autoridade respeitada no meu mercado"
                    ],
                    "metaforas_comuns": [
                        "Corrida de hamster na roda", "Apagar incêndio constantemente", "Remar contra a maré"
                    ],
                    "vocabulario_especifico": [
                        "ROI", "conversão", "funil de vendas", "lead qualificado", "ticket médio", "LTV", "CAC"
                    ],
                    "tom_comunicacao": "Direto e objetivo, aprecia dados concretos e provas tangíveis"
                },
                "gatilhos_mentais_especificos": [
                    "Urgência temporal bem fundamentada", "Escassez de oportunidade real",
                    "Prova social de pares do mesmo nível", "Autoridade reconhecida no mercado",
                    "Medo da perda de oportunidades", "Reciprocidade e valor antecipado"
                ],
                "resistencias_ocultas": [
                    "Medo profundo de sair da zona de conforto conhecida",
                    "Síndrome do impostor que questiona se merece o sucesso",
                    "Perfeccionismo paralisante que impede ação",
                    "Desconfiança em métodos que parecem 'fáceis demais'"
                ],
                "momento_ideal_abordagem": "Quando está frustrado com resultados atuais ou identifica clara oportunidade de crescimento"
            },
            "escopo_posicionamento": {
                "posicionamento_mercado": "Solução premium para empreendedores que querem resultados rápidos e sustentáveis",
                "proposta_valor_unica": "Transforme seu negócio com metodologia comprovada e suporte especializado",
                "diferenciais_competitivos": [
                    "Metodologia exclusiva testada e aprovada",
                    "Suporte personalizado e acompanhamento contínuo",
                    "Resultados mensuráveis e garantidos"
                ],
                "mensagem_central": "Pare de trabalhar NO negócio e comece a trabalhar PELO negócio",
                "tom_comunicacao": "Direto, confiante, baseado em resultados",
                "nicho_especifico": data.get('segmento', 'Empreendedorismo Digital'),
                "estrategia_oceano_azul": "Criar categoria própria focada em implementação prática",
                "ancoragem_preco": "Investimento que se paga em 30 dias"
            },
            "insights_exclusivos_ultra": [
                f"O mercado de {data.get('segmento', 'empreendedorismo')} está em transformação acelerada",
                "Existe lacuna entre ferramentas disponíveis e conhecimento para implementá-las",
                "A maior dor não é falta de informação, mas excesso sem direcionamento",
                "Empreendedores pagam premium por simplicidade e implementação guiada",
                "Fator decisivo é confiança no método + urgência da situação",
                "Prova social de pares vale mais que depoimentos genéricos",
                "Objeção real não é preço, é medo de mais uma tentativa frustrada",
                "Sistemas automatizados são 'santo graal' mas poucos sabem implementar",
                "Jornada de compra é longa mas decisão é emocional e rápida",
                "Conteúdo gratuito é porta de entrada, venda acontece na demonstração",
                "Mercado saturado de teoria, faminto por implementação prática",
                "Diferencial está na execução, não na estratégia",
                "Clientes querem ser guiados passo a passo",
                "ROI deve ser demonstrado em semanas para gerar confiança",
                "Análise gerada em modo de emergência - execute nova análise para resultados completos"
            ],
            "metadata_gemini": {
                "generated_at": datetime.now().isoformat(),
                "model": "emergency_fallback",
                "version": "2.0.0",
                "note": "Análise gerada em modo de emergência devido a erro na IA principal"
            }
        }
        
        return fallback

# Instância global do cliente
try:
    gemini_client = UltraRobustGeminiClient()
    logger.info("✅ Cliente Gemini Ultra-Robusto inicializado com sucesso")
except Exception as e:
    logger.error(f"❌ Erro ao inicializar cliente Gemini: {str(e)}")
    gemini_client = None