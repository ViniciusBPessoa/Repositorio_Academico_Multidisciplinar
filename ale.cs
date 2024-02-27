using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;

public class CodigoEvolucionario : MonoBehaviour
{
    public EvolutionaryStrategy algoritimoEvolucionario;
    public int selecionados;
    public int qtd_geration;
    public GameObject passaro;
    public List<GameObject> jogada;
    // Start is called before the first frame update
    void Start()
    {
        algoritimoEvolucionario = new EvolutionaryStrategy(selecionados);
        inicial_spouwn();
    }

    // Update is called once per frame
    void Update()
    {
        if(verificador_fim())
        {
            termilar_episodio();
        }
    }


    public void inicial_spouwn()
    {
        Vector2 posicao = gameObject.transform.position;
        float modificador = posicao.y;
        for (int i = 0; i < qtd_geration; i++)
        {
            modificador += 0.01f;
            Vector2 posicao2 = new Vector2(posicao.x, modificador);
            Instantiate(passaro, posicao2, Quaternion.identity);
        }
    }

    public void iniciar_segunda()
    {
        PipeSpawner spown = GameObject.FindGameObjectWithTag("Respawn").GetComponent<PipeSpawner>();
        spown.timeSinceLastSpawn = 0f;
        spown.SpawnPipe();

        Vector2 posicao = gameObject.transform.position;
        float modificador = posicao.y;
        for (int i = 0; i < qtd_geration; i++)
        {
            modificador += 0.01f;
            Vector2 posicao2 = new Vector2(posicao.x, modificador);
            Instantiate(passaro, posicao2, Quaternion.identity);
        }
    }

    public bool verificador_fim()
    {
        GameObject[] jogadores = GameObject.FindGameObjectsWithTag("Player");
        bool fim = true;
        
        foreach (GameObject player in jogadores)
        {
            if(player.GetComponent<BirdController>().isDead == false)
            {
                fim = false;
                break;
            }
        }
        return fim;
    }

    public void termilar_episodio()
    {
        GameObject[] jogadores = GameObject.FindGameObjectsWithTag("Player");
        GameObject[] cactos = GameObject.FindGameObjectsWithTag("cactos");
        // algoritimoEvolucionario.generationCreator(jogadores.ToList());

        foreach (GameObject item in jogadores)
        {
            Destroy(item);
        }
        foreach (GameObject item in cactos)
        {
            Destroy(item);
        }
        iniciar_segunda();
        
    }

    public class EvolutionaryStrategy
    {
        [SerializeField] public List<GameObject> atualGeneration;
        int numberSelected;

        public EvolutionaryStrategy(int numberSelected)
        {
            
            this.numberSelected = numberSelected;

        }

        public void generationCreator(List<GameObject> entities)
        {   
            atualGeneration = new List<GameObject>();

            // Ordena a lista de entidades com base no componente "BirdController" e sua variável "score"
            List<GameObject> sortedEntities = entities.OrderBy(entity => {
                BirdController controller = entity.GetComponent<BirdController>();
                return controller != null ? controller.score : 0;
            }).ToList();

            // Seleciona os 'numberSelected' melhores itens da lista ordenada
            List<GameObject> selectedEntities = sortedEntities.Take(numberSelected).ToList();

            // Limpa a lista atual de geração
            atualGeneration.Clear();

            foreach (GameObject entity in selectedEntities)
            {
                if (entity != null)
                {
                    GameObject newBird = GameObject.Instantiate(entity);
                    atualGeneration.Add(newBird);

                    BirdController birdController = newBird.GetComponent<BirdController>();
                    if (birdController != null && birdController.rede_neural != null)
                    {
                        birdController.rede_neural.Train();
                    }
                }
            }
        }

    }
}
