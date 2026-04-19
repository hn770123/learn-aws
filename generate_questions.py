import os
import json

# SAA-C03 の問題データを定義するリスト。
# 各要素は問題の ID、トピック、および詳細な問題内容を含みます。
questions = [
    {
        "id": "q01",
        "topic": "Multi-AZ 構成による RDS の高可用性設計",
        "problem": "ある企業が、Amazon RDS for MySQL を使用して商用環境のデータベースを運用しています。データベースのメンテナンス期間中や、アベイラビリティーゾーン（AZ）の障害が発生した場合でも、アプリケーションのダウンタイムを最小限に抑える必要があります。最も信頼性の高いソリューションはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "リードレプリカを作成し、障害発生時に手動でプライマリインスタンスに昇格させる。"
            },
            {
                "id": "B",
                "text": "Amazon RDS の Multi-AZ 構成を有効にする。"
            },
            {
                "id": "C",
                "text": "データベースのバックアップを定期的に取得し、障害発生時に別の AZ で復元する。"
            },
            {
                "id": "D",
                "text": "EC2 インスタンス上に MySQL を構築し、独自のレプリケーションを構成する。"
            }
        ],
        "answer": "B",
        "explanation": "Amazon RDS の Multi-AZ 構成を有効にすると、別の AZ にスタンバイインスタンスが自動的に作成され、データが同期的にレプリケートされます。プライマリインスタンスの障害やメンテナンス時に、AWS が自動的にフェイルオーバーを行うため、ダウンタイムを最小限に抑えることができます。\n\n*   **Aについて**: リードレプリカは主に読み取り負荷の分散に使用されます。障害時の昇格は手動またはスクリプトによる操作が必要であり、Multi-AZ ほどの自動フェイルオーバー性能はありません。\n*   **Cについて**: バックアップからの復元は時間がかかり、RTO（目標復旧時間）と RPO（目標復旧時点）の要件を満たせない可能性が高いです。\n*   **Dについて**: EC2 自管理の MySQL は管理負荷が高く、RDS の Multi-AZ のような自動化された高可用性を実現するには複雑な設定が必要です。"
    },
    {
        "id": "q02",
        "topic": "S3 ストレージクラスの適切な選択によるコスト最適化",
        "problem": "企業のコンプライアンス要件により、データは長期間保存する必要があります。データは月に1回程度アクセスされますが、アクセスが必要になった際には即座に利用可能である必要があります。最もコスト効率の高い Amazon S3 ストレージクラスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "S3 Standard"
            },
            {
                "id": "B",
                "text": "S3 Standard-IA (Infrequent Access)"
            },
            {
                "id": "C",
                "text": "S3 Glacier Flexible Retrieval"
            },
            {
                "id": "D",
                "text": "S3 One Zone-IA"
            }
        ],
        "answer": "B",
        "explanation": "S3 Standard-IA は、アクセス頻度は低いものの、必要時に即座にアクセスできるデータに最適です。S3 Standard よりもストレージ料金が安く、取り出し料金が発生します。\n\n*   **Aについて**: S3 Standard は頻繁にアクセスされるデータ向けであり、月1回のアクセス頻度ではストレージ料金が割高になります。\n*   **Cについて**: S3 Glacier Flexible Retrieval はアーカイブ向けであり、データの取り出しに数分から数時間かかるため、「即座に利用可能」という要件を満たしません。\n*   **Dについて**: S3 One Zone-IA は単一の AZ に保存するため、他のクラスに比べて耐久性（アベイラビリティーゾーンの消失に対する耐性）が低く、重要なデータの長期保存には不向きな場合があります。"
    },
    {
        "id": "q03",
        "topic": "Amazon SQS を使用したアプリケーションコンポーネントの疎結合化",
        "problem": "ウェブアプリケーションが画像アップロードを受け付け、その後バックエンドで画像処理を行います。トラフィックが急増した際に、フロントエンドの応答性が低下し、画像処理に失敗することがあります。コンポーネントを疎結合化し、信頼性を向上させるための最適な構成はどれですか？",
        "options": [
            {
                "id": "A",
                "text": "フロントエンドからバックエンドの API を直接呼び出し、リトライ処理を実装する。"
            },
            {
                "id": "B",
                "text": "Amazon SQS キューを使用して、フロントエンドがメッセージを送信し、バックエンドがメッセージを処理する。"
            },
            {
                "id": "C",
                "text": "AWS Lambda を使用して、画像を同期的に処理する。"
            },
            {
                "id": "D",
                "text": "Amazon RDS のデータベースをキューとして代用し、ステータスを管理する。"
            }
        ],
        "answer": "B",
        "explanation": "Amazon SQS を使用することで、フロントエンドとバックエンドを疎結合にできます。フロントエンドはメッセージをキューに入れるだけで済み、バックエンドは自身のペースでメッセージを処理できます。トラフィック急増時もキューがバッファとして機能するため、システムの安定性が向上します。\n\n*   **Aについて**: 同期的な呼び出しは疎結合ではなく、負荷が高い場合に依然としてフロントエンドに影響を与えます。\n*   **Cについて**: 同期的な Lambda 呼び出しは、処理時間が長い場合にタイムアウトやエラーの原因となります。\n*   **Dについて**: データベースをメッセージキューとして使用するのはアンチパターンであり、スケーラビリティやパフォーマンスの低下を招きます。"
    },
    {
        "id": "q04",
        "topic": "リージョン間 VPC ピアリングによるプライベート接続の構築",
        "problem": "ある会社は、東京リージョン（ap-northeast-1）とバージニア北部リージョン（us-east-1）の両方に VPC を持っています。これらの VPC 間で機密データを安全に転送する必要があります。インターネットを経由せず、プライベートなネットワーク接続を確立するための最も適切な方法はどれですか？",
        "options": [
            {
                "id": "A",
                "text": "各 VPC にインターネットゲートウェイを設置し、HTTPS で通信する。"
            },
            {
                "id": "B",
                "text": "リージョン間 VPC ピアリング（Inter-Region VPC Peering）を設定する。"
            },
            {
                "id": "C",
                "text": "AWS Direct Connect を使用して両方のリージョンを接続する。"
            },
            {
                "id": "D",
                "text": "各 VPC 間にパブリック IP アドレスを使用した SSH トンネルを構築する。"
            }
        ],
        "answer": "B",
        "explanation": "リージョン間 VPC ピアリングを使用すると、異なる AWS リージョンにある VPC 間でプライベートな IPv4/IPv6 通信が可能になります。トラフィックは AWS のグローバルネットワークバックボーンを経由し、パブリックインターネットを通過しないため、高いセキュリティとパフォーマンスが確保されます。\n\n*   **Aについて**: インターネットゲートウェイ経由の通信はパブリックインターネットを通過します。\n*   **Cについて**: Direct Connect はオンプレミスと AWS 間の接続に使用されるサービスです。VPC 間接続のみの目的としては過剰でコストがかかります。\n*   **Dについて**: パブリック IP を使用した通信はインターネットを経由するため、要件を満たしません。"
    },
    {
        "id": "q05",
        "topic": "AWS Direct Connect と Site-to-Site VPN のハイブリッド接続の使い分け",
        "problem": "オンプレミスのデータセンターから AWS への安定した専用線接続を必要としており、数Gbps の一定した帯域幅を確保したいと考えています。また、セットアップには数週間の猶予があります。最も適切な接続方法はどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Site-to-Site VPN"
            },
            {
                "id": "B",
                "text": "AWS Client VPN"
            },
            {
                "id": "C",
                "text": "AWS Direct Connect"
            },
            {
                "id": "D",
                "text": "Amazon CloudFront"
            }
        ],
        "answer": "C",
        "explanation": "AWS Direct Connect は、オンプレミスから AWS への専用ネットワーク接続を確立するサービスです。インターネットを経由しないため、安定した広帯域（1Gbps、10Gbps 等）を確保でき、一貫したネットワーク体験が提供されます。\n\n*   **Aについて**: Site-to-Site VPN はインターネット経由で暗号化されたトンネルを構築します。セットアップは迅速ですが、インターネットの混雑状況により帯域が不安定になることがあります。\n*   **Bについて**: Client VPN は個々のクライアントデバイスから AWS への接続に使用されます。\n*   **Dについて**: CloudFront はコンテンツ配信ネットワーク（CDN）であり、ハイブリッド接続のためのサービスではありません。"
    },
    {
        "id": "q06",
        "topic": "Amazon CloudFront を使用したグローバルな静的コンテンツ配信の高速化",
        "problem": "世界中のユーザーに対して、S3 バケットに保存されているウェブサイトの画像や動画を低レイテンシーで配信したいと考えています。最も適切なサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon Route 53"
            },
            {
                "id": "B",
                "text": "AWS Global Accelerator"
            },
            {
                "id": "C",
                "text": "Amazon CloudFront"
            },
            {
                "id": "D",
                "text": "Amazon S3 レプリケーション"
            }
        ],
        "answer": "C",
        "explanation": "Amazon CloudFront はコンテンツ配信ネットワーク（CDN）であり、世界各地のエッジロケーションを使用して、ユーザーに近い場所からコンテンツをキャッシュして配信します。これにより、静的コンテンツの配信レイテンシーを大幅に削減できます。\n\n*   **Aについて**: Route 53 は DNS サービスであり、ドメイン解決を行いますが、コンテンツ自体のキャッシュ配信は行いません。\n*   **Bについて**: Global Accelerator は AWS グローバルネットワークを使用して TCP/UDP 通信の経路を最適化しますが、HTTP コンテンツのキャッシュ機能は CloudFront が専門です。\n*   **Dについて**: S3 レプリケーションはデータを別のリージョンにコピーしますが、エッジ配信のような低レイテンシー配信機能はありません。"
    },
    {
        "id": "q07",
        "topic": "AWS WAF を使用した Web アプリケーションへの一般的な攻撃の防御",
        "problem": "Application Load Balancer (ALB) の背後で稼働している Web アプリケーションを、SQL インジェクションやクロスサイトスクリプティング (XSS) などの一般的な Web 攻撃から保護したいと考えています。どのサービスを導入すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Shield Advanced"
            },
            {
                "id": "B",
                "text": "AWS WAF"
            },
            {
                "id": "C",
                "text": "Amazon Inspector"
            },
            {
                "id": "D",
                "text": "Amazon GuardDuty"
            }
        ],
        "answer": "B",
        "explanation": "AWS WAF (Web Application Firewall) は、ALB、Amazon CloudFront、Amazon API Gateway などにデプロイでき、SQL インジェクションや XSS などの一般的なウェブ攻撃をブロックするためのルールを設定できます。\n\n*   **Aについて**: AWS Shield は主に DDoS 攻撃からの保護を提供します。\n*   **Cについて**: Amazon Inspector は EC2 インスタンスやコンテナの脆弱性を診断するサービスです。\n*   **Dについて**: Amazon GuardDuty は AWS アカウントやリソースに対する脅威を継続的にモニタリングするサービスですが、インラインでの攻撃ブロック（ファイアウォール機能）は提供しません。"
    },
    {
        "id": "q08",
        "topic": "Amazon Aurora Global Database を利用した低レイテンシなグローバル展開",
        "problem": "多国籍企業が、地理的に離れた複数のリージョンで読み取り専用のアクティビティをサポートするデータベースを必要としています。災害復旧（DR）のために 1 分未満の目標復旧時間（RTO）を維持しつつ、グローバルな低レイテンシの読み取りを提供できる最適な構成はどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon RDS for MySQL のクロスリージョンリードレプリカ"
            },
            {
                "id": "B",
                "text": "Amazon Aurora Global Database"
            },
            {
                "id": "C",
                "text": "Amazon DynamoDB グローバルテーブル"
            },
            {
                "id": "D",
                "text": "各リージョンに独立した Amazon Aurora クラスターを構築し、アプリ側で同期する。"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Aurora Global Database は、1 つのプライマリリージョンと最大 5 つのセカンダリ読み取り専用リージョンをサポートします。リージョン間のレプリケーションは通常 1 秒未満であり、リージョン全体の障害が発生した場合でも 1 分未満でのフェイルオーバー（昇格）が可能です。\n\n*   **Aについて**: RDS のクロスリージョンレプリケーションは可能ですが、Aurora Global Database ほどパフォーマンスやフェイルオーバー時間は最適化されていません。\n*   **Cについて**: DynamoDB は NoSQL データベースです。要件がリレーショナルデータベース（Aurora の文脈）である場合、Aurora が適切です。\n*   **Dについて**: アプリケーション側での同期は非常に複雑で、整合性の維持が困難です。"
    },
    {
        "id": "q09",
        "topic": "AWS Organizations と SCP による複数アカウントのガバナンス強化",
        "problem": "複数の AWS アカウントを管理している組織において、特定のアカウント群で特定の AWS サービス（例：Amazon Redshift）の使用を禁止したいと考えています。各アカウントのルートユーザーを含めてこの制限を強制するための最も効率的な方法は何ですか？",
        "options": [
            {
                "id": "A",
                "text": "各アカウントの IAM ユーザーに拒否ポリシーを適用する。"
            },
            {
                "id": "B",
                "text": "AWS Organizations を使用し、サービスコントロールポリシー (SCP) を適用する。"
            },
            {
                "id": "C",
                "text": "AWS Config ルールを使用して、禁止されたサービスが作成されたら自動的に削除する。"
            },
            {
                "id": "D",
                "text": "各アカウントの IAM ロールにインラインポリシーをアタッチする。"
            }
        ],
        "answer": "B",
        "explanation": "AWS Organizations のサービスコントロールポリシー (SCP) を使用すると、組織内のアカウントまたは組織単位 (OU) に対して、利用可能なサービスやアクションの最大権限を制限できます。SCP はアカウントのルートユーザーを含むすべてのユーザーに適用されるため、強力なガバナンスを実現できます。\n\n*   **A, Dについて**: IAM ポリシーはアカウント内の個別のエンティティを対象としますが、ルートユーザーを制限することはできません。\n*   **Cについて**: Config ルールは「検出と対応」であり、SCP のような「予防的」な制限（アクション自体の拒否）とは異なります。"
    },
    {
        "id": "q10",
        "topic": "AWS KMS によるデータの暗号化とキー管理戦略",
        "problem": "Amazon S3 に保存される機密データを暗号化する必要があります。コンプライアンス要件により、暗号化キーの作成、回転、およびアクセス制御を完全に管理する必要があり、キーの使用履歴を監査できるようにしなければなりません。どの方法が最適ですか？",
        "options": [
            {
                "id": "A",
                "text": "S3 マネージド型暗号化キー (SSE-S3) を使用する。"
            },
            {
                "id": "B",
                "text": "AWS KMS マネージド型キー (SSE-KMS) を使用する。"
            },
            {
                "id": "C",
                "text": "独自の暗号化アルゴリズムをアプリケーションに実装する。"
            },
            {
                "id": "D",
                "text": "暗号化せずにデータを保存し、VPC ポリシーで保護する。"
            }
        ],
        "answer": "B",
        "explanation": "AWS Key Management Service (AWS KMS) を使用した SSE-KMS は、キーの管理（ローテーション、ポリシーによる制御）を提供し、AWS CloudTrail と連携してキーの使用履歴を監査することができます。\n\n*   **Aについて**: SSE-S3 は AWS がキーを完全に管理し、ユーザーによる細かい制御や詳細な監査ログ（誰がどのデータのためにキーを使ったか等）が KMS ほど柔軟ではありません。\n*   **Cについて**: セキュリティ上のリスクが高く、管理負荷も非常に大きくなります。\n*   **Dについて**: データの暗号化という要件を満たしていません。"
    },
    {
        "id": "q11",
        "topic": "Elastic Load Balancing (ELB) を使用したトラフィックの負荷分散",
        "problem": "Auto Scaling グループ内の複数の EC2 インスタンスで実行されている HTTP ウェブアプリケーションがあります。パスベースのルーティング（例：/api は特定のターゲットグループへ）を実装し、トラフィックを分散させるために最適なロードバランサーの種類はどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Classic Load Balancer"
            },
            {
                "id": "B",
                "text": "Network Load Balancer (NLB)"
            },
            {
                "id": "C",
                "text": "Application Load Balancer (ALB)"
            },
            {
                "id": "D",
                "text": "Gateway Load Balancer"
            }
        ],
        "answer": "C",
        "explanation": "Application Load Balancer (ALB) は OSI 参照モデルの第 7 層（アプリケーション層）で動作し、HTTP/HTTPS トラフィックのパスベースルーティングやホストベースルーティングなどの高度なルーティング機能をサポートしています。\n\n*   **Aについて**: Classic Load Balancer は旧世代であり、パスベースルーティングなどの高度な機能はありません。\n*   **Bについて**: NLB は第 4 層（トランスポート層）で動作し、高パフォーマンスで低レイテンシーな TCP/UDP 通信に適していますが、URL パスによるルーティングは行いません。\n*   **Dについて**: Gateway Load Balancer は、サードパーティの仮想アプライアンス（ファイアウォール等）のデプロイと管理に使用されます。"
    },
    {
        "id": "q12",
        "topic": "Auto Scaling グループによる EC2 インスタンスの動的スケーリング",
        "problem": "Web アプリケーションの CPU 使用率が 70% を超えたときに EC2 インスタンスを自動的に追加し、負荷が下がったときに削減したいと考えています。この動作を実現するために Amazon EC2 Auto Scaling で設定すべきものはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "スケジュールされたスケーリングポリシー"
            },
            {
                "id": "B",
                "text": "ターゲット追跡スケーリングポリシー"
            },
            {
                "id": "C",
                "text": "手動スケーリング"
            },
            {
                "id": "D",
                "text": "予測スケーリングポリシー"
            }
        ],
        "answer": "B",
        "explanation": "ターゲット追跡スケーリングポリシーを使用すると、「CPU 使用率を平均 70% に維持する」といった目標値を設定するだけで、Auto Scaling が自動的にインスタンスの増減を調整します。\n\n*   **Aについて**: スケジュールされたスケーリングは、特定の時間（例：月曜日の朝 9 時）にインスタンス数を変更する場合に使用します。\n*   **Cについて**: 手動スケーリングは自動化されていません。\n*   **Dについて**: 予測スケーリングは、過去のトラフィックパターンに基づき、将来の負荷を予測して事前にスケーリングを行う機能です。"
    },
    {
        "id": "q13",
        "topic": "Amazon EFS を使用した複数 EC2 インスタンス間での共有ストレージ",
        "problem": "複数の Linux EC2 インスタンスが、同時にアクセスして読み書きできる共有ファイルシステムを必要としています。標準的なファイルシステムインターフェースをサポートし、データが複数の AZ にまたがって保存されるマネージドサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon EBS (Elastic Block Store)"
            },
            {
                "id": "B",
                "text": "Amazon EFS (Elastic File System)"
            },
            {
                "id": "C",
                "text": "Amazon S3"
            },
            {
                "id": "D",
                "text": "Amazon EC2 インスタンスストア"
            }
        ],
        "answer": "B",
        "explanation": "Amazon EFS は、複数の EC2 インスタンス（およびオンプレミスサーバー）から同時にマウント可能な共有ファイルストレージを提供します。NFS プロトコルをサポートし、データはリージョン内の複数の AZ に自動的に保存されるため、高い可用性と耐久性を備えています。\n\n*   **Aについて**: 標準的な EBS ボリュームは一度に 1 つのインスタンスにのみアタッチ可能です（Multi-Attach 機能を持つ一部のボリュームタイプもありますが、Linux の標準的な共有ファイルシステムとしての利用は EFS が一般的です）。\n*   **Cについて**: S3 はオブジェクトストレージであり、標準的なファイルシステム（ディレクトリ構造やファイルのロック等）として直接マウントして使用するには不向きです。\n*   **Dについて**: インスタンスストアは特定の EC2 インスタンスに物理的にアタッチされた一時的なストレージであり、共有はできません。"
    },
    {
        "id": "q14",
        "topic": "AWS Storage Gateway を利用したオンプレミスとクラウドの連携",
        "problem": "オンプレミスのアプリーションから、NFS プロトコルを使用して AWS 上の S3 にデータをバックアップしたいと考えています。低レイテンシーなアクセスのために、頻繁に使用されるデータはローカルにキャッシュする必要があります。どの Storage Gateway タイプを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "ボリュームゲートウェイ（保管型）"
            },
            {
                "id": "B",
                "text": "テープゲートウェイ"
            },
            {
                "id": "C",
                "text": "S3 ファイルゲートウェイ"
            },
            {
                "id": "D",
                "text": "FSx ファイルゲートウェイ"
            }
        ],
        "answer": "C",
        "explanation": "S3 ファイルゲートウェイを使用すると、NFS や SMB プロトコルを使用して Amazon S3 上にファイルをオブジェクトとして保存できます。頻繁にアクセスされるデータはローカルのゲートウェイにキャッシュされるため、高速なアクセスが可能です。\n\n*   **Aについて**: ボリュームゲートウェイは iSCSI 接続を提供し、ブロックストレージとして使用されます。\n*   **Bについて**: テープゲートウェイは物理的なテープライブラリの代替として使用されます。\n*   **Dについて**: FSx ファイルゲートウェイは Amazon FSx for Windows File Server へのアクセスを提供します。"
    },
    {
        "id": "q15",
        "topic": "Amazon Route 53 によるフェイルオーバールーティングの設定",
        "problem": "プライマリのリージョンにある Web サーバーがダウンした場合に、自動的にセカンダリのリージョンにある静的なバックアップサイト（S3 でホスト）にトラフィックを切り替えたいと考えています。Route 53 でどのルーティングポリシーを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "シンプルルーティング"
            },
            {
                "id": "B",
                "text": "加重ルーティング"
            },
            {
                "id": "C",
                "text": "フェイルオーバールーティング"
            },
            {
                "id": "D",
                "text": "レイテンシールーティング"
            }
        ],
        "answer": "C",
        "explanation": "フェイルオーバールーティングポリシーは、ヘルスチェックの結果に基づいて、正常なリソース（プライマリが異常な場合はセカンダリ）にトラフィックを転送します。アクティブ/パッシブ構成の実現に最適です。\n\n*   **Aについて**: シンプルルーティングは 1 つのリソースにマッピングするだけで、ヘルスチェックによる切り替えは行いません。\n*   **Bについて**: 加重ルーティングは、指定した比率（例：80:20）でトラフィックを分散させます。\n*   **Dについて**: レイテンシールーティングは、ユーザーにとって最も遅延の少ないリージョンにトラフィックを転送します。"
    },
    {
        "id": "q16",
        "topic": "AWS Lambda と API Gateway を組み合わせたサーバーレスアーキテクチャ",
        "problem": "インフラの管理を最小限に抑えつつ、ユーザーからの HTTP リクエストに応じてビジネスロジックを実行するスケーラブルな Web バックエンドを構築したいと考えています。最も適切な組み合わせはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "EC2 インスタンスと Application Load Balancer"
            },
            {
                "id": "B",
                "text": "Amazon API Gateway と AWS Lambda"
            },
            {
                "id": "C",
                "text": "Amazon S3 と CloudFront"
            },
            {
                "id": "D",
                "text": "AWS Elastic Beanstalk と Amazon RDS"
            }
        ],
        "answer": "B",
        "explanation": "Amazon API Gateway と AWS Lambda を組み合わせることで、サーバーのプロビジョニングや管理をすることなく、API エンドポイントを作成し、リクエストに応じてコードを実行するサーバーレスアーキテクチャを構築できます。これは高いスケーラビリティとコスト効率（実行分のみの支払い）を提供します。\n\n*   **A, Dについて**: EC2 や Beanstalk はサーバーの管理（パッチ適用やスケーリング設定等）が必要になります。\n*   **Cについて**: S3 と CloudFront は主に静的コンテンツの配信に使用されます。"
    },
    {
        "id": "q17",
        "topic": "AWS Shield による DDoS 攻撃からのインフラ保護",
        "problem": "AWS 上で稼働するアプリケーションに対して、大規模な Distributed Denial of Service (DDoS) 攻撃からの高度な保護と、攻撃発生時の AWS 24/7 サポートチームへのアクセスを必要としています。どのサービスプランを選択すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Shield Standard"
            },
            {
                "id": "B",
                "text": "AWS Shield Advanced"
            },
            {
                "id": "C",
                "text": "AWS WAF"
            },
            {
                "id": "D",
                "text": "AWS Firewall Manager"
            }
        ],
        "answer": "B",
        "explanation": "AWS Shield Advanced は、Shield Standard で提供される基本的な保護に加え、より大規模で高度な DDoS 攻撃からの保護、攻撃に対するリアルタイムレポート、および AWS シールドレスポンスチーム (SRT) へのアクセスを提供します。\n\n*   **Aについて**: Shield Standard はすべての AWS ユーザーに無料で提供される基本的な DDoS 保護ですが、SRT へのアクセスや詳細なレポートは含まれません。\n*   **Cについて**: AWS WAF はアプリケーション層 (L7) の攻撃を防ぎますが、インフラ層の DDoS 保護は Shield が担当します。\n*   **Dについて**: Firewall Manager は複数のアカウントにまたがる WAF や Shield の設定を一元管理するサービスです。"
    },
    {
        "id": "q18",
        "topic": "Amazon EBS ボリュームタイプ（gp3, io2等）のパフォーマンス特性に基づく選択",
        "problem": "高い I/O パフォーマンスを必要とするリレーショナルデータベースを EC2 上で実行しています。プロビジョニングされた IOPS を最大 64,000 以上必要とし、非常に高い耐久性を求めています。最も適切な EBS ボリュームタイプはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "汎用 SSD (gp3)"
            },
            {
                "id": "B",
                "text": "スループット最適化 HDD (st1)"
            },
            {
                "id": "C",
                "text": "プロビジョニングされた IOPS SSD (io2 Block Express)"
            },
            {
                "id": "D",
                "text": "Cold HDD (sc1)"
            }
        ],
        "answer": "C",
        "explanation": "io2 Block Express は、ミリ秒未満の低レイテンシーと、最大 256,000 IOPS、4,000 MB/s のスループットを提供し、最も要求の厳しいデータベースワークロード向けに設計されています。\n\n*   **Aについて**: gp3 はコスト効率に優れた汎用ストレージですが、最大 IOPS は 16,000 までです。\n*   **B, Dについて**: HDD タイプは I/O 集中型ではなく、スループットやコスト重視のデータアクセスに適しています。"
    },
    {
        "id": "q19",
        "topic": "VPC エンドポイント（インターフェイス/ゲートウェイ）を使用した AWS サービスへのセキュアな接続",
        "problem": "プライベートサブネット内にある EC2 インスタンスから、パブリックインターネットを経由せずに Amazon S3 にアクセスしたいと考えています。コストを最小限に抑えつつ、この要件を満たすために最適な VPC エンドポイントのタイプはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "インターフェイスエンドポイント (AWS PrivateLink)"
            },
            {
                "id": "B",
                "text": "ゲートウェイエンドポイント"
            },
            {
                "id": "C",
                "text": "クライアント VPN エンドポイント"
            },
            {
                "id": "D",
                "text": "サイト間 VPN エンドポイント"
            }
        ],
        "answer": "B",
        "explanation": "Amazon S3 および DynamoDB に対しては、ゲートウェイ型の VPC エンドポイントを無料で使用できます。これはルートテーブルにエントリを追加することで機能し、インターネットゲートウェイや NAT ゲートウェイを介さずにプライベートな通信を可能にします。\n\n*   **Aについて**: インターフェイスエンドポイント（PrivateLink）も S3 で利用可能ですが、時間あたりの料金とデータ処理料金が発生するため、コスト最小化の観点ではゲートウェイ型が優先されます。\n*   **C, Dについて**: これらは VPC と外部ネットワークを接続するためのものであり、VPC 内から S3 への接続には適しません。"
    },
    {
        "id": "q20",
        "topic": "AWS Backup を使用したリソース横断的なバックアップの一元管理",
        "problem": "Amazon EBS ボリューム、RDS データベース、および Amazon EFS ファイルシステムのバックアップを、一元的なポリシーに基づいて自動的に取得・管理したいと考えています。どのサービスを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Backup"
            },
            {
                "id": "B",
                "text": "Amazon Data Lifecycle Manager (DLM)"
            },
            {
                "id": "C",
                "text": "AWS Storage Gateway"
            },
            {
                "id": "D",
                "text": "AWS CloudFormation"
            }
        ],
        "answer": "A",
        "explanation": "AWS Backup は、複数の AWS サービス（EBS, RDS, EFS, DynamoDB, EC2 等）にわたるデータのバックアップを一元的に自動化および管理できるフルマネージドサービスです。\n\n*   **Bについて**: Data Lifecycle Manager は主に EBS ボリュームのスナップショットや AMI の管理に特化しており、EFS や RDS 全体を統合管理するものではありません。\n*   **Cについて**: Storage Gateway はオンプレミスと AWS の接続用です。\n*   **Dについて**: CloudFormation はインフラのプロビジョニング用であり、バックアップの定常的な管理サービスではありません。"
    },
    {
        "id": "q21",
        "topic": "AWS Config によるリソースの変更履歴の記録とコンプライアンス監査",
        "problem": "AWS アカウント内のリソース構成の変更を追跡し、特定の設定（例：すべての S3 バケットが公開されていないこと）に準拠しているかどうかを継続的に監査する必要があります。どのサービスが最適ですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS CloudTrail"
            },
            {
                "id": "B",
                "text": "Amazon CloudWatch"
            },
            {
                "id": "C",
                "text": "AWS Config"
            },
            {
                "id": "D",
                "text": "AWS Trusted Advisor"
            }
        ],
        "answer": "C",
        "explanation": "AWS Config は、AWS リソースの設定を評価、監査、審査するためのサービスです。リソースの設定変更を記録し、定義したルール（Config ルール）に従ってコンプライアンス状態を評価します。\n\n*   **Aについて**: CloudTrail は「誰が・いつ・何をしたか」という API コールのログを記録しますが、リソースの設定状態の評価は行いません。\n*   **Bについて**: CloudWatch はパフォーマンスメトリクスやログの監視に使用されます。\n*   **Dについて**: Trusted Advisor はコスト削減やセキュリティのベストプラクティスをアドバイスしますが、詳細な設定変更履歴の追跡やカスタムルールの評価は Config が専門です。"
    },
    {
        "id": "q22",
        "topic": "Amazon FSx for Windows File Server による高可用なファイル共有",
        "problem": "Windows サーバーベースのアプリケーションがあり、SMB プロトコルを介してアクセスできる完全マネージドな共有ファイルストレージを必要としています。Active Directory と統合し、高可用性を実現するために最適なサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon EFS"
            },
            {
                "id": "B",
                "text": "Amazon FSx for Windows File Server"
            },
            {
                "id": "C",
                "text": "Amazon S3"
            },
            {
                "id": "D",
                "text": "Amazon EBS Multi-Attach"
            }
        ],
        "answer": "B",
        "explanation": "Amazon FSx for Windows File Server は、Windows ファイルシステム上に構築されたフルマネージドの共有ストレージを提供し、SMB プロトコル、Active Directory 統合、および Multi-AZ 展開による高可用性をサポートしています。\n\n*   **Aについて**: Amazon EFS は Linux ワークロード（NFS）向けです。\n*   **Cについて**: S3 はオブジェクトストレージであり、標準的な SMB 共有としては機能しません。\n*   **Dについて**: EBS Multi-Attach は一部のボリュームを複数インスタンスにアタッチできますが、ファイルシステムとしての共有管理（ロック等）はユーザーが行う必要があります。"
    },
    {
        "id": "q23",
        "topic": "AWS Glue と Amazon S3 を使用したデータレイクの構築",
        "problem": "Amazon S3 に保存されている大量の非構造化データを分析するために、データのスキーマを自動的に検出し、カタログ化したいと考えています。どのサービスを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Glue Data Catalog"
            },
            {
                "id": "B",
                "text": "Amazon Athena"
            },
            {
                "id": "C",
                "text": "AWS Batch"
            },
            {
                "id": "D",
                "text": "Amazon Redshift"
            }
        ],
        "answer": "A",
        "explanation": "AWS Glue は、データの抽出、変換、ロード (ETL) を行うフルマネージドサービスです。Glue クローラーを使用すると、S3 などのデータソースをスキャンしてスキーマを自動的に検出し、AWS Glue Data Catalog にメタデータを保存できます。\n\n*   **Bについて**: Athena は S3 上のデータを SQL でクエリするサービスですが、カタログ管理自体は Glue Data Catalog を利用します。\n*   **Cについて**: AWS Batch はバッチ処理の実行管理用です。\n*   **Dについて**: Redshift はデータウェアハウスであり、データのカタログ化（スキーマ検出）に特化したサービスではありません。"
    },
    {
        "id": "q24",
        "topic": "Amazon Redshift による大規模データウェアハウスの設計",
        "problem": "ペタバイト規模の構造化データを対象に、複雑なクエリを実行してビジネスインテリジェンス (BI) レポートを作成する必要があります。高いクエリパフォーマンスを実現するための最も適切なマネージドサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon RDS for PostgreSQL"
            },
            {
                "id": "B",
                "text": "Amazon Aurora"
            },
            {
                "id": "C",
                "text": "Amazon Redshift"
            },
            {
                "id": "D",
                "text": "Amazon ElastiCache"
            }
        ],
        "answer": "C",
        "explanation": "Amazon Redshift は、ペタバイト規模のデータウェアハウスサービスであり、カラムナ（列指向）ストレージや並列処理（MPP）を使用して、大規模なデータセットに対する複雑な分析クエリを高速に実行できます。\n\n*   **A, Bについて**: これらは OLTP（オンライン事務処理）向けのデータベースであり、大規模な分析クエリ（OLAP）には Redshift の方が適しています。\n*   **Dについて**: ElastiCache はインメモリキャッシュであり、永続的な大規模データウェアハウスではありません。"
    },
    {
        "id": "q25",
        "topic": "AWS Step Functions を使用したマイクロサービスのワークフロー調整",
        "problem": "複数の AWS Lambda 関数、Amazon SNS、およびオンプレミスのシステムを含む複雑な注文処理ワークフローを構築しています。各ステップの実行順序を管理し、エラー発生時のリトライロジックを視覚的に定義・運用するために最適なサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Step Functions"
            },
            {
                "id": "B",
                "text": "Amazon SQS"
            },
            {
                "id": "C",
                "text": "AWS Lambda デスティネーション"
            },
            {
                "id": "D",
                "text": "Amazon EventBridge"
            }
        ],
        "answer": "A",
        "explanation": "AWS Step Functions は、AWS サービスを組み合わせてサーバーレスなワークフローを構築できるオーケストレーションサービスです。ステートマシンを使用して各ステップの順序や条件分岐、エラー処理を定義でき、実行状態を視覚的に確認できます。\n\n*   **Bについて**: SQS はメッセージのキューイングによる疎結合化を提供しますが、ワークフロー全体のステート管理や順序制御機能はありません。\n*   **Cについて**: Lambda デスティネーションは関数の実行結果を次に渡すことができますが、複雑な条件分岐や複数のサービスにまたがるオーケストレーションには向きません。\n*   **Dについて**: EventBridge はイベント駆動型アーキテクチャのためのイベントバスであり、ステートフルなワークフロー管理サービスではありません。"
    },
    {
        "id": "q26",
        "topic": "AWS Batch による大規模なバッチコンピューティングの実行",
        "problem": "数百から数千の計算集中型バッチジョブを実行する必要があります。ジョブの要求に応じて EC2 インスタンスや Fargate のプロビジョニング、スケジューリング、および実行を自動的に管理したいと考えています。どのサービスが最適ですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Lambda"
            },
            {
                "id": "B",
                "text": "AWS Batch"
            },
            {
                "id": "C",
                "text": "Amazon EC2 Auto Scaling"
            },
            {
                "id": "D",
                "text": "AWS Glue"
            }
        ],
        "answer": "B",
        "explanation": "AWS Batch は、開発者やエンジニア、データサイエンティストが、数万件のバッチコンピューティングジョブを AWS で効率的に実行できるようにするサービスです。コンピューティングリソースのプロビジョニングを自動的に行い、キューイングとスケジューリングを管理します。\n\n*   **Aについて**: Lambda は短時間の処理には向いていますが、長時間の大規模なバッチジョブには制限があります。\n*   **Cについて**: Auto Scaling はインスタンスの増減を管理しますが、ジョブのキューイングやスケジューリング機能は持っていません。\n*   **Dについて**: AWS Glue は主にデータ ETL 用であり、汎用的なバッチコンピューティングジョブ（例：科学計算やシミュレーション）には Batch が適しています。"
    },
    {
        "id": "q27",
        "topic": "Amazon ElastiCache (Redis/Memcached) を利用したデータベースの負荷軽減",
        "problem": "読み取り負荷の高いソーシャルメディアアプリケーションのパフォーマンスを向上させ、データベース（RDS）のレイテンシーを削減したいと考えています。頻繁にアクセスされるデータをメモリ内にキャッシュするために最適なサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon CloudFront"
            },
            {
                "id": "B",
                "text": "Amazon ElastiCache"
            },
            {
                "id": "C",
                "text": "Amazon DynamoDB Accelerator (DAX)"
            },
            {
                "id": "D",
                "text": "Amazon S3 Transfer Acceleration"
            }
        ],
        "answer": "B",
        "explanation": "Amazon ElastiCache (Redis または Memcached) を使用すると、頻繁にアクセスされるデータをミリ秒未満の応答時間でメモリから提供できるため、プライマリデータベースの読み取り負荷を大幅に軽減できます。\n\n*   **Aについて**: CloudFront はエッジでのコンテンツ配信（主に HTTP 静的コンテンツ）に使用されます。\n*   **Cについて**: DAX は DynamoDB 専用のインメモリキャッシュであり、RDS の負荷軽減には ElastiCache が適しています。\n*   **Dについて**: S3 Transfer Acceleration は S3 へのアップロード/ダウンロードを高速化するものです。"
    },
    {
        "id": "q28",
        "topic": "Amazon Kinesis Data Streams を利用したリアルタイムデータの収集と処理",
        "problem": "数千の IoT デバイスから送信される継続的なログデータをリアルタイムで収集し、複数の消費者アプリケーションで同時に処理・分析する必要があります。順序付けを維持しつつ、高いスループットを処理できるサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon SQS"
            },
            {
                "id": "B",
                "text": "Amazon Kinesis Data Streams"
            },
            {
                "id": "C",
                "text": "Amazon Kinesis Data Firehose"
            },
            {
                "id": "D",
                "text": "Amazon SNS"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Kinesis Data Streams は、大規模なデータストリームをリアルタイムで収集・処理するためのサービスです。シャードを使用してスケーリングし、複数のアプリケーションが同じストリームからデータを独立して処理でき、シャード内での順序も維持されます。\n\n*   **Aについて**: SQS はメッセージキューイングですが、複数の消費者が同じメッセージを同時に受け取ること（ファンアウト）は Kinesis ほどネイティブに最適化されていません（SNS+SQS を組み合わせる必要があります）。\n*   **Cについて**: Firehose はデータを S3 や Redshift 等に「配信」することに特化しており、リアルタイムの多目的処理には Data Streams が適しています。\n*   **Dについて**: SNS はプッシュ型の通知サービスであり、ストリームデータの保持や再読み込みはできません。"
    },
    {
        "id": "q29",
        "topic": "AWS Transfer Family による S3 へのセキュアなファイル転送",
        "problem": "既存のビジネスプロセスで SFTP プロトコルを使用してファイルを交換しています。インフラの管理をせずに、SFTP 経由で直接 Amazon S3 にファイルをアップロード・ダウンロードできるようにするには、どのサービスを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Storage Gateway"
            },
            {
                "id": "B",
                "text": "AWS Transfer Family"
            },
            {
                "id": "C",
                "text": "AWS DataSync"
            },
            {
                "id": "D",
                "text": "Amazon S3 マルチパートアップロード"
            }
        ],
        "answer": "B",
        "explanation": "AWS Transfer Family は、SFTP、FTPS、および FTP を使用して Amazon S3 または Amazon EFS との間でファイルを直接転送できるようにするフルマネージドサービスです。既存のプロトコルを維持しつつ、サーバー管理の負担をなくすことができます。\n\n*   **Aについて**: Storage Gateway も NFS/SMB を提供しますが、SFTP サーバーをマネージドで提供するわけではありません。\n*   **Cについて**: DataSync はオンラインデータ転送の高速化ツールであり、定常的な SFTP インターフェースを提供するものではありません。\n*   **Dについて**: マルチパートアップロードは S3 API の機能であり、SFTP プロトコルとは異なります。"
    },
    {
        "id": "q30",
        "topic": "AWS Global Accelerator を使用したグローバルなアプリケーションのパフォーマンス向上",
        "problem": "世界中のユーザーが、単一のリージョンで稼働しているゲームサーバーに接続しています。インターネットのルーティングの不安定さを解消し、ユーザーにより一貫した低レイテンシーな体験を提供しつつ、固定の IP アドレスを提供したいと考えています。どのサービスが最適ですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon CloudFront"
            },
            {
                "id": "B",
                "text": "AWS Global Accelerator"
            },
            {
                "id": "C",
                "text": "Amazon Route 53 レイテンシールーティング"
            },
            {
                "id": "D",
                "text": "AWS Direct Connect"
            }
        ],
        "answer": "B",
        "explanation": "AWS Global Accelerator は、AWS のグローバルネットワークを使用して、ユーザーからアプリケーションへのパスを最適化します。2 つの静的な Anycast IP アドレスを提供し、エッジロケーションから AWS バックボーン経由でトラフィックを運ぶため、インターネットの混雑による遅延や変動を抑えることができます。\n\n*   **Aについて**: CloudFront は主に HTTP コンテンツのキャッシュに使用されます。Global Accelerator は非 HTTP プロトコル（ゲームの UDP/TCP 通信等）の高速化にも適しています。\n*   **Cについて**: Route 53 は最適なリージョンの IP を返しますが、そこまでの通信経路自体はパブリックインターネットに依存します。\n*   **Dについて**: Direct Connect は特定の拠点と AWS 間の専用線であり、不特定多数のグローバルユーザー向けではありません。"
    },
    {
        "id": "q31",
        "topic": "Amazon Athena を使用した S3 上のデータの標準 SQL による分析",
        "problem": "Amazon S3 に保存されている大量のログファイルを、サーバーをプロビジョニングせずに標準 SQL を使用して直接分析したいと考えています。最もコスト効率が高く、管理負荷の低いサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon Redshift"
            },
            {
                "id": "B",
                "text": "Amazon Athena"
            },
            {
                "id": "C",
                "text": "Amazon EMR"
            },
            {
                "id": "D",
                "text": "Amazon RDS"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Athena は、Amazon S3 内のデータを標準 SQL を使用して簡単に分析できるインタラクティブなクエリサービスです。サーバーレスであるため、インフラの管理は不要で、実行したクエリに対してのみ料金が発生します。\n\n*   **Aについて**: Redshift はデータウェアハウスであり、データのロードが必要で、クラスターの管理も発生します。\n*   **Cについて**: EMR は Hadoop エコシステムを利用した大規模データ処理用ですが、クラスターのプロビジョニングと管理が必要です。\n*   **Dについて**: RDS はリレーショナルデータベースであり、S3 上のファイルを直接 SQL でクエリする用途には向きません。"
    },
    {
        "id": "q32",
        "topic": "AWS AppSync を使用したマネージドな GraphQL API の構築",
        "problem": "モバイルおよび Web アプリケーション向けに、複数のデータソース（DynamoDB、Lambda、HTTP API）からのデータを統合し、リアルタイムの更新機能を提供する GraphQL API を構築する必要があります。どのサービスが最適ですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon API Gateway"
            },
            {
                "id": "B",
                "text": "AWS AppSync"
            },
            {
                "id": "C",
                "text": "AWS Amplify"
            },
            {
                "id": "D",
                "text": "Amazon QuickSight"
            }
        ],
        "answer": "B",
        "explanation": "AWS AppSync は、GraphQL を使用してアプリケーションが正確に必要なデータだけに簡単にアクセスできるようにするフルマネージドサービスです。複数のデータソースからのデータ集約を容易にし、WebSocket を使用したリアルタイムのデータ同期をネイティブにサポートしています。\n\n*   **Aについて**: API Gateway は REST API の構築には適していますが、GraphQL 特有の機能や複雑なデータ集約を AppSync ほど容易には提供しません。\n*   **Cについて**: Amplify はフレームワークおよびツールセットであり、バックエンドとして AppSync を利用しますが、API サービス自体は AppSync です。\n*   **Dについて**: QuickSight はビジネスインテリジェンス（可視化）ツールです。"
    },
    {
        "id": "q33",
        "topic": "AWS Control Tower を使用したランディングゾーンのセットアップ",
        "problem": "複数の AWS アカウントを持つ組織において、セキュリティとコンプライアンスのベストプラクティスに基づいた「ランディングゾーン」と呼ばれる管理環境を、自動的にセットアップおよび管理したいと考えています。どのサービスを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Organizations"
            },
            {
                "id": "B",
                "text": "AWS Control Tower"
            },
            {
                "id": "C",
                "text": "AWS Config"
            },
            {
                "id": "D",
                "text": "AWS CloudFormation StackSets"
            }
        ],
        "answer": "B",
        "explanation": "AWS Control Tower は、複数の AWS アカウントを持つ環境を、ベストプラクティスに従って簡単にセットアップおよび統制するためのサービスです。ガバナンスのためのガードレール（制約）を自動的に適用し、ダッシュボードで各アカウントの準拠状況を確認できます。\n\n*   **Aについて**: Organizations は複数アカウント管理の基盤ですが、Control Tower はその上でベストプラクティスを自動適用する上位のオーケストレーションサービスです。\n*   **Cについて**: Config は個別のリソース設定を監視するサービスです。\n*   **Dについて**: StackSets は複数アカウントへの展開に使用されるツールですが、環境全体のガバナンスフレームワークを自動構築するものではありません。"
    },
    {
        "id": "q34",
        "topic": "Amazon GuardDuty による脅威検出しとセキュリティモニタリング",
        "problem": "AWS アカウント、ワークロード、および S3 内のデータを保護するために、悪意のあるアクティビティや不正な動作を継続的にモニタリングするマネージド型の脅威検出サービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Shield"
            },
            {
                "id": "B",
                "text": "Amazon Inspector"
            },
            {
                "id": "C",
                "text": "Amazon GuardDuty"
            },
            {
                "id": "D",
                "text": "AWS WAF"
            }
        ],
        "answer": "C",
        "explanation": "Amazon GuardDuty は、機械学習、異常検知、および悪意のある IP アドレスやドメインのリストを使用して、AWS アカウントやリソースに対する脅威を継続的にモニタリングする脅威検出サービスです。VPC フローログ、CloudTrail ログ、DNS ログなどを分析します。\n\n*   **Aについて**: Shield は DDoS 保護サービスです。\n*   **Bについて**: Inspector は EC2 やコンテナのソフトウェアの脆弱性をスキャンするサービスです。\n*   **Dについて**: WAF はウェブアプリケーションファイアウォールです。"
    },
    {
        "id": "q35",
        "topic": "Amazon Inspector による EC2 インスタンスの脆弱性診断",
        "problem": "EC2 インスタンスや Amazon ECR 内のコンテナイメージに対して、ソフトウェアの脆弱性や意図しないネットワークの露出がないかを自動的に評価したいと考えています。どのサービスを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon GuardDuty"
            },
            {
                "id": "B",
                "text": "Amazon Inspector"
            },
            {
                "id": "C",
                "text": "AWS Trusted Advisor"
            },
            {
                "id": "D",
                "text": "Amazon Macie"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Inspector は、自動化された脆弱性管理サービスであり、EC2 インスタンス、コンテナイメージ (ECR)、および Lambda 関数を継続的にスキャンして、ソフトウェアの脆弱性や意図しないネットワーク露出を検出します。\n\n*   **Aについて**: GuardDuty は実行中の脅威（不正アクセス等）を検出するサービスです。\n*   **Cについて**: Trusted Advisor はコスト、パフォーマンス、セキュリティのベストプラクティスを助言しますが、詳細なソフトウェア脆弱性スキャンは行いません。\n*   **Dについて**: Macie は S3 内の機密データの検出に特化しています。"
    },
    {
        "id": "q36",
        "topic": "AWS Lake Formation を使用したセキュアなデータレイクの管理",
        "problem": "Amazon S3 上にデータレイクを構築する際、データのクリーニング、カタログ化、および複雑なアクセス制御（列レベルの権限設定など）を一元的に管理したいと考えています。どのサービスが最適ですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Glue"
            },
            {
                "id": "B",
                "text": "Amazon Athena"
            },
            {
                "id": "C",
                "text": "AWS Lake Formation"
            },
            {
                "id": "D",
                "text": "Amazon Redshift Spectrum"
            }
        ],
        "answer": "C",
        "explanation": "AWS Lake Formation は、セキュアなデータレイクを数日で簡単にセットアップできるサービスです。データのクロール、クリーニングを行い、Glue Data Catalog を通じてテーブルや列レベルのきめ細かなアクセス制御を一元的に定義できます。\n\n*   **Aについて**: Glue は ETL とデータカタログ機能を提供しますが、Lake Formation はそれらをオーケストレートし、高度なセキュリティ管理を付加します。\n*   **Bについて**: Athena はクエリサービスです。\n*   **Dについて**: Redshift Spectrum は S3 上のデータを Redshift からクエリする機能です。"
    },
    {
        "id": "q37",
        "topic": "Amazon Macie による S3 上の機密データの自動検出",
        "problem": "Amazon S3 に保存されている大量のデータの中から、個人情報 (PII) や機密データを機械学習を用いて自動的に検出し、保護するためのサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon GuardDuty"
            },
            {
                "id": "B",
                "text": "Amazon Macie"
            },
            {
                "id": "C",
                "text": "AWS KMS"
            },
            {
                "id": "D",
                "text": "AWS CloudTrail"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Macie は、フルマネージドなデータセキュリティおよびデータプライバシーサービスで、機械学習とパターンマッチングを使用して Amazon S3 内の機密データを自動的に検出、分類、および保護します。\n\n*   **Aについて**: GuardDuty はアカウントやネットワークレベルの脅威検出です。\n*   **Cについて**: KMS は暗号化キーの管理サービスです。\n*   **Dについて**: CloudTrail は API ログの記録です。"
    },
    {
        "id": "q38",
        "topic": "AWS Outposts によるオンプレミスへの AWS サービスの展開",
        "problem": "低レイテンシーが求められるローカル処理や、データのローカル保存要件のために、AWS のインフラストラクチャとサービスをオンプレミスのデータセンターで実行したいと考えています。どのサービスを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Direct Connect"
            },
            {
                "id": "B",
                "text": "AWS Snowball Edge"
            },
            {
                "id": "C",
                "text": "AWS Outposts"
            },
            {
                "id": "D",
                "text": "AWS Local Zones"
            }
        ],
        "answer": "C",
        "explanation": "AWS Outposts は、AWS のサービス、インフラストラクチャ、および運用モデルをオンプレミスの施設に提供するフルマネージドサービスです。AWS と同じ API、ツール、ハードウェアを使用して、ハイブリッド体験を実現できます。\n\n*   **Aについて**: Direct Connect は専用ネットワーク接続です。\n*   **Bについて**: Snowball Edge はデータ移行やエッジコンピューティング用ですが、常設のインフラ拡張としては Outposts が適しています。\n*   **Dについて**: Local Zones は、特定の都市に近い AWS のインフラ拡張ですが、ユーザーのオンプレミス施設に設置するものではありません。"
    },
    {
        "id": "q39",
        "topic": "Amazon Rekognition を使用した画像・動画分析の統合",
        "problem": "アプリケーションに画像や動画の分析機能を追加し、物体検出、顔認識、不適切なコンテンツのフィルタリングを自動化したいと考えています。機械学習の深い知識なしに利用できるサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon SageMaker"
            },
            {
                "id": "B",
                "text": "Amazon Rekognition"
            },
            {
                "id": "C",
                "text": "Amazon Comprehend"
            },
            {
                "id": "D",
                "text": "Amazon Polly"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Rekognition を使用すると、画像や動画の分析をアプリケーションに簡単に統合できます。学習済みのモデルが API 経由で提供されるため、物体、人、テキスト、不適切なコンテンツなどを容易に検出できます。\n\n*   **Aについて**: SageMaker は独自の機械学習モデルを構築・訓練・デプロイするためのプラットフォームです。\n*   **Cについて**: Comprehend はテキスト分析（自然言語処理）用です。\n*   **Dについて**: Polly はテキストを音声に変換するサービスです。"
    },
    {
        "id": "q40",
        "topic": "AWS App Mesh によるマイクロサービス間の通信管理",
        "problem": "多数のマイクロサービス間の通信を標準化し、一貫した可視性、トラフィック制御、およびセキュリティを提供するためのサービスメッシュ機能を提供するサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS App Mesh"
            },
            {
                "id": "B",
                "text": "Elastic Load Balancing (ELB)"
            },
            {
                "id": "C",
                "text": "Amazon API Gateway"
            },
            {
                "id": "D",
                "text": "AWS Cloud Map"
            }
        ],
        "answer": "A",
        "explanation": "AWS App Mesh は、サービスメッシュを提供し、マイクロサービス間の通信を容易に管理できるようにします。サイドカープロキシ (Envoy) を使用して、アプリケーションコードを変更せずに、通信の可視化、再試行ロジック、トラフィックの分散、暗号化を実現します。\n\n*   **Bについて**: ELB は外部からのトラフィック分散が主目的です。\n*   **Cについて**: API Gateway は外部に公開する API の管理です。\n*   **Dについて**: Cloud Map はリソースの検出（サービスディスカバリ）サービスです。"
    },
    {
        "id": "q41",
        "topic": "Amazon Managed Streaming for Apache Kafka (MSK) の活用",
        "problem": "既存の Apache Kafka アプリケーションを変更せずに、AWS 上で Kafka クラスターを管理・実行したいと考えています。インフラの管理負荷を軽減できるフルマネージドサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon Kinesis Data Streams"
            },
            {
                "id": "B",
                "text": "Amazon Managed Streaming for Apache Kafka (MSK)"
            },
            {
                "id": "C",
                "text": "Amazon SQS"
            },
            {
                "id": "D",
                "text": "Amazon MQ"
            }
        ],
        "answer": "B",
        "explanation": "Amazon MSK は、Apache Kafka を使用してストリーミングデータを処理するアプリケーションを簡単に構築・実行できるフルマネージドサービスです。Kafka のオープンソース互換性を維持しているため、既存のコードやツールをそのまま使用できます。\n\n*   **Aについて**: Kinesis Data Streams は AWS 独自のストリーミングサービスであり、Kafka とは互換性がありません。\n*   **Cについて**: SQS はメッセージキューサービスです。\n*   **Dについて**: Amazon MQ は ActiveMQ や RabbitMQ などのメッセージブローカー用のマネージドサービスです。"
    },
    {
        "id": "q42",
        "topic": "AWS App Runner によるコンテナ化された Web アプリの迅速なデプロイ",
        "problem": "インフラやスケーリングの管理を一切行わずに、コンテナ化された Web アプリケーションや API サービスをソースコードやコンテナイメージから直接デプロイしたいと考えています。最もシンプルなサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon ECS (Elastic Container Service)"
            },
            {
                "id": "B",
                "text": "Amazon EKS (Elastic Kubernetes Service)"
            },
            {
                "id": "C",
                "text": "AWS App Runner"
            },
            {
                "id": "D",
                "text": "AWS Elastic Beanstalk"
            }
        ],
        "answer": "C",
        "explanation": "AWS App Runner は、コンテナ化された Web アプリケーションや API を大規模にすばやくデプロイするためのフルマネージドサービスです。サーバー、ロードバランサー、CI/CD パイプラインなどのインフラ設定を自動化し、開発者がコードに集中できるようにします。\n\n*   **A, Bについて**: ECS や EKS はより詳細なコントロールが可能ですが、クラスターやタスク定義などの設定管理が必要です。\n*   **Dについて**: Elastic Beanstalk は Web アプリのデプロイ用ですが、コンテナに特化した App Runner の方がコンテナワークロードにはよりシンプルです。"
    },
    {
        "id": "q43",
        "topic": "Amazon DynamoDB のプロビジョニング済み容量とオンデマンド容量の選択",
        "problem": "予測不能なスパイクを伴うワークロードがあり、事前のキャパシティプランニングなしにリクエストに応じて自動的にスケーリングする DynamoDB の料金設定モデルはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "プロビジョニング済み容量モード"
            },
            {
                "id": "B",
                "text": "オンデマンド容量モード"
            },
            {
                "id": "C",
                "text": "リザーブド容量"
            },
            {
                "id": "D",
                "text": "スポット容量"
            }
        ],
        "answer": "B",
        "explanation": "DynamoDB のオンデマンド容量モードは、以前のトラフィックレベルに関係なく、1 秒間に数千のリクエストを処理できる柔軟なオプションです。リクエストごとに支払う形式で、予測困難なトラフィックに対して最も効率的です。\n\n*   **Aについて**: プロビジョニング済み容量は、読み取り/書き込みの 1 秒あたりのユニット数を事前に設定する必要があります。\n*   **Cについて**: リザーブド容量は、プロビジョニング済み容量を長期契約で安く利用する仕組みです。\n*   **Dについて**: DynamoDB にスポット容量という概念はありません（EC2 等にはあります）。"
    },
    {
        "id": "q44",
        "topic": "AWS CloudTrail によるユーザーアクティビティと API コールのログ記録",
        "problem": "AWS アカウント全体のガバナンス、コンプライアンス、およびリスク監査のために、誰が、いつ、どのリソースに対して、どの API を呼び出したかを記録・保存するためのサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon CloudWatch"
            },
            {
                "id": "B",
                "text": "AWS Config"
            },
            {
                "id": "C",
                "text": "AWS CloudTrail"
            },
            {
                "id": "D",
                "text": "AWS Trusted Advisor"
            }
        ],
        "answer": "C",
        "explanation": "AWS CloudTrail は、AWS アカウントのガバナンス、コンプライアンス、操作監査、リスク監査を可能にするサービスです。ユーザー、ロール、または AWS サービスによって実行されたアクション（API コール）をイベントとしてログに記録します。\n\n*   **Aについて**: CloudWatch はパフォーマンスメトリクスやログメッセージの監視用です。\n*   **Bについて**: Config はリソースの設定状態（Inventory）の記録と評価用です。\n*   **Dについて**: Trusted Advisor はベストプラクティスのアドバイスを提供します。"
    },
    {
        "id": "q45",
        "topic": "Amazon Cognito による Web/モバイルアプリのユーザー認証と認可",
        "problem": "Web やモバイルアプリケーションに、サインアップ、サインイン、およびアクセスコントロールの機能を簡単に追加したいと考えています。ソーシャルログイン（Google, Facebook等）や、SAML 2.0 による ID 連携をサポートしているサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS IAM"
            },
            {
                "id": "B",
                "text": "Amazon Cognito"
            },
            {
                "id": "C",
                "text": "AWS Organizations"
            },
            {
                "id": "D",
                "text": "AWS Directory Service"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Cognito を使用すると、Web アプリやモバイルアプリに迅速かつ簡単にユーザーのサインアップ/サインインおよびアクセスコントロール機能を追加できます。ユーザープール（ID 保存）と ID プール（AWS リソースへのアクセス許可）の機能を提供します。\n\n*   **Aについて**: IAM は主に AWS リソースを管理する従業員等の権限管理に使用されます。\n*   **Cについて**: Organizations は複数アカウントの管理用です。\n*   **Dについて**: Directory Service は Active Directory などを AWS 上で展開・連携するためのものです。"
    },
    {
        "id": "q46",
        "topic": "AWS Directory Service による既存の Active Directory との統合",
        "problem": "AWS 上で Microsoft Active Directory を直接実行したい、あるいはオンプレミスの AD と AWS サービスを連携させて、ユーザーが既存の企業資格情報を使用して AWS アプリケーションにログインできるようにしたいと考えています。どのサービスを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon Cognito"
            },
            {
                "id": "B",
                "text": "AWS IAM"
            },
            {
                "id": "C",
                "text": "AWS Directory Service"
            },
            {
                "id": "D",
                "text": "AWS Single Sign-On (AWS IAM Identity Center)"
            }
        ],
        "answer": "C",
        "explanation": "AWS Directory Service (AWS Managed Microsoft AD) を使用すると、AWS 上でマネージドな Active Directory を実行できます。既存のオンプレミス AD との信頼関係を構築し、シームレスなドメイン参加やシングルサインオンを実現できます。\n\n*   **Aについて**: Cognito は B2C アプリケーションのユーザー管理に主に使われます。\n*   **Dについて**: IAM Identity Center は複数アカウントへのアクセス管理用で、バックエンドとして Directory Service を利用することがあります。"
    },
    {
        "id": "q47",
        "topic": "Amazon WorkSpaces による仮想デスクトップ環境の提供",
        "problem": "従業員に対して、どこからでも、どのデバイスからでもアクセスできる、セキュアでマネージドな Windows または Linux の仮想デスクトップ環境を提供したいと考えています。どのサービスが最適ですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon AppStream 2.0"
            },
            {
                "id": "B",
                "text": "Amazon WorkSpaces"
            },
            {
                "id": "C",
                "text": "Amazon EC2"
            },
            {
                "id": "D",
                "text": "AWS Client VPN"
            }
        ],
        "answer": "B",
        "explanation": "Amazon WorkSpaces は、フルマネージドのデスクトップ仮想化サービス（DaaS）です。ユーザーは使い慣れたデスクトップ環境に様々なデバイスからアクセスでき、データはデバイス上ではなく AWS クラウド内に保持されるため、セキュリティも向上します。\n\n*   **Aについて**: AppStream 2.0 はデスクトップ全体ではなく、特定の「アプリケーション」を配信することに特化しています。\n*   **Cについて**: EC2 はサーバーのプロビジョニング用であり、デスクトップ環境としての集中管理機能は提供しません。\n*   **Dについて**: Client VPN は VPC へのリモートアクセス用です。"
    },
    {
        "id": "q48",
        "topic": "AWS Transit Gateway を使用したハブ・アンド・スポーク型のネットワーク構成",
        "problem": "多数の VPC およびオンプレミスネットワークを相互接続する必要があります。VPC 間のピアリング接続が複雑になりすぎる（フルメッシュ問題）のを防ぎ、中央でルーティングを管理できる「ハブ」として機能するサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "VPC ピアリング"
            },
            {
                "id": "B",
                "text": "AWS Transit Gateway"
            },
            {
                "id": "C",
                "text": "AWS Direct Connect Gateway"
            },
            {
                "id": "D",
                "text": "AWS PrivateLink"
            }
        ],
        "answer": "B",
        "explanation": "AWS Transit Gateway は、中央のハブを介して何千もの VPC やオンプレミスネットワークを接続できるネットワーク中継ハブです。ネットワークのトポロジーを簡素化し、管理の複雑さを大幅に軽減します。\n\n*   **Aについて**: VPC ピアリングは 1 対 1 の接続であり、数が増えると管理が非常に困難になります。\n*   **Cについて**: Direct Connect Gateway は、Direct Connect を複数の VPC/リージョンに接続するためのものです。\n*   **Dについて**: PrivateLink は特定のサービスをプライベートに公開するためのものです。"
    },
    {
        "id": "q49",
        "topic": "Amazon VPC ネットワーク ACL とセキュリティグループの使い分け",
        "problem": "VPC 内のセキュリティ設計において、サブネットレベルで動作し、ステートレスにトラフィックを制御する（インバウンドとアウトバウンドの両方に明示的な許可ルールが必要）コンポーネントはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "セキュリティグループ"
            },
            {
                "id": "B",
                "text": "ネットワーク ACL"
            },
            {
                "id": "C",
                "text": "インターネットゲートウェイ"
            },
            {
                "id": "D",
                "text": "ルートテーブル"
            }
        ],
        "answer": "B",
        "explanation": "ネットワーク ACL（アクセスコントロールリスト）は、1 つ以上のサブネットの境界で動作し、ファイアウォールとして機能するステートレスなセキュリティレイヤーです。\n\n*   **Aについて**: セキュリティグループはインスタンスレベルで動作し、ステートフル（許可されたインバウンドに対するアウトバウンドは自動で許可される）です。\n*   **Cについて**: インターネットゲートウェイは VPC とインターネット間の通信用コンポーネントです。\n*   **Dについて**: ルートテーブルはパケットの配送先を決定します。"
    },
    {
        "id": "q50",
        "topic": "AWS PrivateLink を使用したサービスのセキュアな共有",
        "problem": "自分の VPC 内にある SaaS アプリケーションを、パブリックインターネットに公開することなく、他の AWS 顧客の VPC とプライベートに共有したいと考えています。最もセキュアでスケーラブルな方法はどれですか？",
        "options": [
            {
                "id": "A",
                "text": "VPC ピアリング"
            },
            {
                "id": "B",
                "text": "AWS Transit Gateway"
            },
            {
                "id": "C",
                "text": "AWS PrivateLink"
            },
            {
                "id": "D",
                "text": "AWS Site-to-Site VPN"
            }
        ],
        "answer": "C",
        "explanation": "AWS PrivateLink を使用すると、サービスを VPC エンドポイントサービスとして公開し、他のユーザーが自分の VPC 内にインターフェイスエンドポイントを作成することで、そのサービスにプライベートにアクセスできるようになります。IP アドレスの重複を気にする必要がなく、高いセキュリティを確保できます。\n\n*   **A, Bについて**: これらはネットワーク全体を接続するため、IP 範囲の重複不可などの制約があり、不特定多数へのサービス提供には向きません。\n*   **Dについて**: VPN は拠点間接続用です。"
    },
    {
        "id": "q51",
        "topic": "Amazon S3 オブジェクトロックによる WORM ストレージの実装",
        "problem": "金融機関のコンプライアンス要件により、特定のデータを一定期間、いかなるユーザー（ルートユーザーを含む）も削除や上書きができないように保存する必要があります。この WORM (Write Once Read Many) モデルを実現するために、Amazon S3 で設定すべき機能は何ですか？",
        "options": [
            {
                "id": "A",
                "text": "S3 バージョニング"
            },
            {
                "id": "B",
                "text": "S3 バケットポリシーによる拒否"
            },
            {
                "id": "C",
                "text": "S3 オブジェクトロック"
            },
            {
                "id": "D",
                "text": "S3 ライフサイクルポリシー"
            }
        ],
        "answer": "C",
        "explanation": "Amazon S3 オブジェクトロックを使用すると、オブジェクトが一定期間、または無期限に削除や上書きされるのを防ぐことができます。コンプライアンスモードを使用すれば、ルートユーザーであっても削除不可になります。\n\n*   **Aについて**: バージョニングは上書き時に古いデータを残しますが、削除自体を完全に防ぐ（防止）ものではありません。\n*   **Bについて**: ポリシーは強力ですが、ルートユーザーが変更できてしまうため、厳密な WORM 要件には不十分です。\n*   **Dについて**: ライフサイクルポリシーはデータの移行や削除を「自動化」するもので、削除を「防止」するものではありません。"
    },
    {
        "id": "q52",
        "topic": "AWS Trusted Advisor によるコスト削減とセキュリティ向上の推奨事項",
        "problem": "AWS 環境全体をスキャンし、コストの削減、パフォーマンスの向上、セキュリティの強化、および耐障害性の向上に関する具体的なアドバイスと推奨事項をリアルタイムで提供してくれるサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Config"
            },
            {
                "id": "B",
                "text": "AWS Trusted Advisor"
            },
            {
                "id": "C",
                "text": "Amazon Inspector"
            },
            {
                "id": "D",
                "text": "AWS Health Dashboard"
            }
        ],
        "answer": "B",
        "explanation": "AWS Trusted Advisor は、AWS のベストプラクティスに従ってリソースを最適化するのに役立つオンラインツールです。使用率の低い EC2 インスタンスの特定（コスト）、公開されている S3 バケットのチェック（セキュリティ）など、多岐にわたるチェック項目を提供します。\n\n*   **Aについて**: Config は設定の変更履歴とコンプライアンスの追跡用です。\n*   **Cについて**: Inspector は脆弱性診断（ソフトウェアレベル）に特化しています。\n*   **Dについて**: Health Dashboard は AWS サービス自体の障害やメンテナンス情報を通知します。"
    },
    {
        "id": "q53",
        "topic": "Amazon EventBridge を使用したイベント駆動型アーキテクチャ",
        "problem": "S3 へのファイルアップロード、EC2 の状態変更、あるいは独自アプリケーションからのカスタムイベントをトリガーにして、Lambda 関数や SQS などの複数のターゲットに処理を配信する、サーバーレスなイベントバスサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon SNS"
            },
            {
                "id": "B",
                "text": "Amazon SQS"
            },
            {
                "id": "C",
                "text": "Amazon EventBridge"
            },
            {
                "id": "D",
                "text": "Amazon Kinesis Data Streams"
            }
        ],
        "answer": "C",
        "explanation": "Amazon EventBridge は、アプリケーション、統合された SaaS アプリケーション、および AWS サービスからのデータを使用して、イベント駆動型アプリケーションを大規模に構築しやすくするサーバーレスイベントバスです。\n\n*   **Aについて**: SNS はプッシュ通知サービスですが、EventBridge の方が高度なフィルタリングや SaaS 連携、スケジュール実行などの機能が豊富です。\n*   **Bについて**: SQS はメッセージキューイング用です。\n*   **Dについて**: Kinesis は大規模なストリーミングデータのリアルタイム処理用です。"
    },
    {
        "id": "q54",
        "topic": "AWS Resource Access Manager (RAM) を使用したリソース共有",
        "problem": "AWS Organizations を使用している組織において、あるアカウントで作成した Transit Gateway や VPC サブネットを、他のアカウントと安全に共有して利用させたいと考えています。どのサービスを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS PrivateLink"
            },
            {
                "id": "B",
                "text": "VPC ピアリング"
            },
            {
                "id": "C",
                "text": "AWS Resource Access Manager (RAM)"
            },
            {
                "id": "D",
                "text": "AWS Organizations SCP"
            }
        ],
        "answer": "C",
        "explanation": "AWS Resource Access Manager (RAM) を使用すると、AWS リソースを AWS アカウント間で安全に共有できます。これにより、リソースの重複作成を避け、コストを抑えつつ、管理を一元化できます。\n\n*   **Aについて**: PrivateLink はサービス（アプリケーション）へのプライベートアクセスを提供します。\n*   **Bについて**: VPC ピアリングはネットワークを接続しますが、サブネットそのものを共有するわけではありません。\n*   **Dについて**: SCP は権限を制限するポリシーです。"
    },
    {
        "id": "q55",
        "topic": "Amazon SES によるアプリケーションからのメール送信",
        "problem": "マーケティングキャンペーンのメール、注文確認の通知、およびその他のトランザクションメールを、高い到達率で安価に送信・受信するためのクラウドベースの E メール送信サービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon SNS"
            },
            {
                "id": "B",
                "text": "Amazon SES (Simple Email Service)"
            },
            {
                "id": "C",
                "text": "Amazon SQS"
            },
            {
                "id": "D",
                "text": "AWS Pinpoint"
            }
        ],
        "answer": "B",
        "explanation": "Amazon SES は、開発者が任意のアプリケーション内からメールを送信できるように設計された、スケーラブルでコスト効率の高い E メール送信サービスです。\n\n*   **Aについて**: SNS もメール送信が可能ですが、主にシステム通知用であり、本格的なメールマーケティングや大量のトランザクションメールには SES が適しています。\n*   **Cについて**: SQS はメッセージキューです。\n*   **Dについて**: Pinpoint もメールを使用しますが、より高度な顧客分析やエンゲージメント（プッシュ、SMS 含）に特化した上位サービスです。"
    },
    {
        "id": "q56",
        "topic": "AWS CloudFormation を使用したインフラストラクチャのコード化 (IaC)",
        "problem": "JSON または YAML 形式のテンプレートを使用して、AWS のインフラストラクチャ全体を定義し、繰り返し可能で一貫した方法でリソースをプロビジョニング・管理したいと考えています。どのサービスを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Systems Manager"
            },
            {
                "id": "B",
                "text": "AWS Elastic Beanstalk"
            },
            {
                "id": "C",
                "text": "AWS CloudFormation"
            },
            {
                "id": "D",
                "text": "AWS OpsWorks"
            }
        ],
        "answer": "C",
        "explanation": "AWS CloudFormation は、インフラストラクチャをコードとして扱う (IaC) ためのサービスです。テンプレートファイルを作成することで、スタックとして関連する AWS リソースのグループを自動的に作成・更新・削除できます。\n\n*   **Aについて**: Systems Manager は運用タスクの自動化やインスタンス管理用です。\n*   **Bについて**: Elastic Beanstalk はアプリケーションの迅速な展開用ですが、裏側で CloudFormation を利用することがあります。\n*   **Dについて**: OpsWorks は Chef や Puppet を使用した構成管理サービスです。"
    },
    {
        "id": "q57",
        "topic": "AWS Elastic Beanstalk による迅速な Web アプリケーション展開",
        "problem": "Java、.NET、PHP、Python などの Web アプリケーションを、容量のプロビジョニング、負荷分散、スケーリング、ヘルスモニタリングの詳細を気にせずに AWS 上に迅速にデプロイして管理したいと考えています。どのサービスが最適ですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Lambda"
            },
            {
                "id": "B",
                "text": "AWS App Runner"
            },
            {
                "id": "C",
                "text": "AWS Elastic Beanstalk"
            },
            {
                "id": "D",
                "text": "Amazon EC2"
            }
        ],
        "answer": "C",
        "explanation": "AWS Elastic Beanstalk は、Web アプリケーションやサービスをデプロイおよびスケーリングするための使いやすいサービスです。コードをアップロードするだけで、Beanstalk が自動的に容量のプロビジョニング、負荷分散、Auto Scaling、およびアプリケーションの状態監視を処理します。\n\n*   **Aについて**: Lambda はサーバーレスな関数実行用です。\n*   **Bについて**: App Runner はコンテナ化された Web アプリに特化しています。\n*   **Dについて**: EC2 はより細かい制御が必要な場合に適しており、管理負荷は高くなります。"
    },
    {
        "id": "q58",
        "topic": "Amazon EMR を使用したビッグデータ処理クラスターの運用",
        "problem": "Apache Hadoop、Spark、Presto、HBase などのオープンソースツールを使用して、膨大な量のデータを並列処理するためのマネージド型クラスタープラットフォームはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon Redshift"
            },
            {
                "id": "B",
                "text": "Amazon Athena"
            },
            {
                "id": "C",
                "text": "Amazon EMR"
            },
            {
                "id": "D",
                "text": "AWS Glue"
            }
        ],
        "answer": "C",
        "explanation": "Amazon EMR は、AWS 上でビッグデータフレームワークを簡単に実行できる業界最先端のクラウドビッグデータプラットフォームです。EC2 インスタンスのクラスターを自動的にセットアップし、大規模な計算処理を実行できます。\n\n*   **Aについて**: Redshift はデータウェアハウスです。\n*   **Bについて**: Athena は S3 上のデータに対するインタラクティブなクエリ用です。\n*   **Dについて**: Glue はサーバーレスな ETL サービスです。"
    },
    {
        "id": "q59",
        "topic": "AWS Ground Station を使用した衛星データの下り回線制御",
        "problem": "自社で地上局を建設・管理することなく、AWS のグローバルな地上局ネットワークを使用して、衛星との通信、データの受信・処理を直接行いたいと考えています。どのサービスを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Outposts"
            },
            {
                "id": "B",
                "text": "AWS Snowball Edge"
            },
            {
                "id": "C",
                "text": "AWS Ground Station"
            },
            {
                "id": "D",
                "text": "Amazon Kinesis"
            }
        ],
        "answer": "C",
        "explanation": "AWS Ground Station は、衛星通信を制御し、データをダウンリンク（受信）し、衛星の運用をスケールできるフルマネージドサービスです。利用した分だけ料金を支払うモデルで、高価な自社地上局を必要としません。\n\n*   **Aについて**: Outposts はオンプレミス用インフラです。\n*   **Bについて**: Snowball Edge はデータ移行用です。\n*   **Dについて**: Kinesis は受信した後のストリームデータ処理に使用される可能性があります。"
    },
    {
        "id": "q60",
        "topic": "Amazon Honeycode によるノーコードアプリ開発",
        "problem": "プログラミングコードを書くことなく、スプレッドシートのような操作感でカスタムの Web およびモバイルアプリケーションを作成し、チームの業務プロセスを管理したいと考えています。どのサービスを使用すべきですか？（※注：現在は新規受付終了またはサービス終了の方向にある場合がありますが、試験範囲に含まれる可能性があります）",
        "options": [
            {
                "id": "A",
                "text": "AWS AppSync"
            },
            {
                "id": "B",
                "text": "Amazon Honeycode"
            },
            {
                "id": "C",
                "text": "AWS Amplify"
            },
            {
                "id": "D",
                "text": "Amazon QuickSight"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Honeycode は、プログラミングを学ばなくてもカスタムアプリを構築できるノーコードプラットフォームです。スプレッドシートモデルに基づいて、データの管理や通知機能を備えたアプリを作成できます。\n\n*   **Aについて**: AppSync は GraphQL API 開発用です。\n*   **Cについて**: Amplify は開発者向けのフレームワークです。\n*   **Dについて**: QuickSight はデータ可視化ツールです。"
    },
    {
        "id": "q61",
        "topic": "AWS IoT Core によるデバイスとクラウド間の安全な通信",
        "problem": "数百万台の IoT デバイスを安全に接続し、メッセージをクラウドや他のデバイスにルーティングするためのサービスはどれですか？MQTT や HTTP などのプロトコルをサポートしており、デバイスがオフラインの時も状態を保持できる「デバイスシャドウ」機能を持っています。",
        "options": [
            {
                "id": "A",
                "text": "Amazon Kinesis"
            },
            {
                "id": "B",
                "text": "AWS IoT Core"
            },
            {
                "id": "C",
                "text": "AWS Direct Connect"
            },
            {
                "id": "D",
                "text": "Amazon SQS"
            }
        ],
        "answer": "B",
        "explanation": "AWS IoT Core は、コネクテッドデバイスが簡単かつ安全にクラウドアプリケーションやその他のデバイスとやり取りできるようにするマネージドクラウドサービスです。MQTT, HTTP, WebSockets をサポートし、メッセージブローカーやデバイスシャドウなどの機能を提供します。\n\n*   **Aについて**: Kinesis はストリーミングデータの「処理」用で、デバイスとの双方向通信の管理には IoT Core が適しています。\n*   **Cについて**: Direct Connect は専用線接続です。\n*   **Dについて**: SQS はメッセージキューですが、数百万のデバイスとの直接的な双方向通信用ではありません。"
    },
    {
        "id": "q62",
        "topic": "Amazon MQ によるマネージド型メッセージブローカーの移行",
        "problem": "オンプレミスで ActiveMQ や RabbitMQ を使用しており、コードを大幅に書き換えることなく AWS に移行したいと考えています。これらの業界標準のメッセージングプロトコルをサポートするマネージドサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon SQS"
            },
            {
                "id": "B",
                "text": "Amazon SNS"
            },
            {
                "id": "C",
                "text": "Amazon MQ"
            },
            {
                "id": "D",
                "text": "Amazon Kinesis"
            }
        ],
        "answer": "C",
        "explanation": "Amazon MQ は、Apache ActiveMQ や RabbitMQ などの一般的なメッセージブローカー向けの管理型メッセージブローカーサービスです。既存のアプリケーションで使用されている JMS, NMS, AMQP, STOMP, MQTT, WebSocket などのプロトコルと互換性があるため、移行が容易です。\n\n*   **A, Bについて**: SQS や SNS は AWS 独自の API を使用するため、既存のオープンソースベースのコードを書き換える必要があります。\n*   **Dについて**: Kinesis はリアルタイムストリーム処理用です。"
    },
    {
        "id": "q63",
        "topic": "Amazon Panorama によるエッジでのビデオ分析",
        "problem": "オンプレミスに設置されたカメラからの映像をリアルタイムで分析し、コンピュータービジョンを使用して、店舗の客足のカウントや製造ラインの異常検知をオフラインに近い環境（エッジ）で行いたいと考えています。どのサービスを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon Rekognition"
            },
            {
                "id": "B",
                "text": "Amazon Kinesis Video Streams"
            },
            {
                "id": "C",
                "text": "Amazon Panorama"
            },
            {
                "id": "D",
                "text": "AWS DeepLens"
            }
        ],
        "answer": "C",
        "explanation": "Amazon Panorama は、オンプレミスのインターネットプロトコル (IP) カメラにコンピュータービジョン (CV) を追加できる機械学習 (ML) アプライアンスおよびソフトウェア開発キット (SDK) です。データをクラウドに送信せずにローカルで分析できるため、低レイテンシーが実現できます。\n\n*   **Aについて**: Rekognition はクラウドベースの画像・動画分析サービスです。\n*   **Bについて**: Kinesis Video Streams は動画データのストリーミングと保存用です。\n*   **Dについて**: DeepLens は開発者向けの学習用カメラデバイスです。"
    },
    {
        "id": "q64",
        "topic": "Amazon QuickSight によるビジネスインテリジェンスと可視化",
        "problem": "組織内のユーザーが、S3, RDS, Redshift などの様々なデータソースからデータを読み取り、インタラクティブなダッシュボードを作成して、機械学習による異常検知や予測を含めたインサイトを共有できるようにするためのサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon Athena"
            },
            {
                "id": "B",
                "text": "Amazon QuickSight"
            },
            {
                "id": "C",
                "text": "AWS Glue"
            },
            {
                "id": "D",
                "text": "Amazon SageMaker"
            }
        ],
        "answer": "B",
        "explanation": "Amazon QuickSight は、高速でクラウドネイティブなビジネスインテリジェンス (BI) サービスです。データを視覚化し、インタラクティブなダッシュボードを構築して、組織内の全員にインサイトを提供できます。SPICE という高速なインメモリエンジンを搭載しています。\n\n*   **Aについて**: Athena は SQL クエリサービスです。\n*   **Cについて**: Glue は ETL サービスです。\n*   **Dについて**: SageMaker は機械学習モデルの構築用です。"
    },
    {
        "id": "q65",
        "topic": "AWS Snowball Edge を使用した大規模データ移行",
        "problem": "数百テラバイトから数ペタバイトのデータを Amazon S3 に移行する必要があります。ネットワーク帯域が限られており、インターネット経由の転送には数ヶ月かかる見込みです。物理デバイスを使用してデータを安全に輸送し、クラウドへ移行するための最適なサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS DataSync"
            },
            {
                "id": "B",
                "text": "AWS Storage Gateway"
            },
            {
                "id": "C",
                "text": "AWS Snowball Edge"
            },
            {
                "id": "D",
                "text": "AWS Direct Connect"
            }
        ],
        "answer": "C",
        "explanation": "AWS Snowball Edge は、データの収集、処理、および移行に使用される物理的なストレージデバイスです。ネットワーク経由の転送が非現実的なほどの大容量データを、デバイスを郵送することで短時間かつ安全に AWS へ移行できます。\n\n*   **Aについて**: DataSync はオンライン転送の高速化ツールです。\n*   **Bについて**: Storage Gateway はハイブリッドストレージサービスです。\n*   **Dについて**: Direct Connect は専用線ですが、敷設に時間がかかり、極端に大量のデータの一時的な移行には Snowball が向く場合があります。"
    },
    {
        "id": "q66",
        "topic": "Amazon Managed Grafana によるメトリクスとログの可視化",
        "problem": "オープンソースの Grafana を使用して、CloudWatch、Prometheus、その他の様々なデータソースからのメトリクスを一元的に視覚化したいと考えています。Grafana サーバーの管理をせずに利用できる AWS のサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon CloudWatch Dashboards"
            },
            {
                "id": "B",
                "text": "Amazon Managed Grafana"
            },
            {
                "id": "C",
                "text": "Amazon Managed Service for Prometheus"
            },
            {
                "id": "D",
                "text": "Amazon QuickSight"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Managed Grafana は、一般的なオープンソースの視覚化ツールである Grafana のフルマネージドサービスです。サーバーのプロビジョニングやパッチ適用をせずに、複数のデータソースからのメトリクス、ログ、トレースを分析・可視化できます。\n\n*   **Aについて**: CloudWatch 独自のダッシュボードですが、Grafana の高度な可視化機能や外部ソースとの統合を求める場合は Grafana が選ばれます。\n*   **Cについて**: Prometheus 自体のマネージドサービスであり、視覚化には Grafana 等と組み合わせます。\n*   **Dについて**: QuickSight はビジネスデータ分析（BI）用です。"
    },
    {
        "id": "q67",
        "topic": "AWS AppFlow を使用した SaaS と AWS サービス間のデータ連携",
        "problem": "Salesforce、Zendesk、Slack などの SaaS アプリケーションと、Amazon S3 や Amazon Redshift などの AWS サービスの間で、コードを書かずに安全にデータを転送・同期したいと考えています。どのサービスを使用すべきですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Glue"
            },
            {
                "id": "B",
                "text": "Amazon EventBridge"
            },
            {
                "id": "C",
                "text": "AWS AppFlow"
            },
            {
                "id": "D",
                "text": "AWS Step Functions"
            }
        ],
        "answer": "C",
        "explanation": "AWS AppFlow は、SaaS アプリケーションと AWS サービス間のデータ転送を安全に自動化するフルマネージドな統合サービスです。パブリックインターネットを経由せずに転送するように構成でき、データのマッピングや加工も容易です。\n\n*   **Aについて**: Glue は ETL サービスですが、SaaS との連携には AppFlow の方がより特化しており簡単です。\n*   **Bについて**: EventBridge はイベントのルーティング用です。\n*   **Dについて**: Step Functions はワークフローのオーケストレーション用です。"
    },
    {
        "id": "q68",
        "topic": "Amazon Braket による量子コンピューティングの実験",
        "problem": "量子コンピューティングのアルゴリズムを構築、テスト、および実行するために、複数の量子ハードウェアプロバイダーの技術に共通のインターフェースでアクセスできるサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon SageMaker"
            },
            {
                "id": "B",
                "text": "Amazon Braket"
            },
            {
                "id": "C",
                "text": "AWS Batch"
            },
            {
                "id": "D",
                "text": "Amazon High Performance Computing (HPC)"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Braket は、量子コンピューティングを加速させるためのフルマネージドサービスです。量子アルゴリズムを設計・シミュレートし、さまざまな形式の量子ハードウェア（QPU）で実行するための開発環境を提供します。\n\n*   **Aについて**: 機械学習用です。\n*   **Cについて**: バッチ処理用です。\n*   **Dについて**: HPC は従来の高速計算（スーパーコンピュータ的）なワークロード用です。"
    },
    {
        "id": "q69",
        "topic": "AWS Compute Optimizer による適切なインスタンスサイズの推奨",
        "problem": "EC2 インスタンス、EBS ボリューム、Lambda 関数などの使用状況を機械学習で分析し、コスト削減やパフォーマンス向上のために最適なリソースタイプやサイズ（オーバープロビジョニングの解消など）を提案してくれるサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Trusted Advisor"
            },
            {
                "id": "B",
                "text": "AWS Cost Explorer"
            },
            {
                "id": "C",
                "text": "AWS Compute Optimizer"
            },
            {
                "id": "D",
                "text": "Amazon CloudWatch"
            }
        ],
        "answer": "C",
        "explanation": "AWS Compute Optimizer は、AWS のリソース構成を分析し、機械学習を活用して最適な AWS リソースを推奨するサービスです。過去のメトリクスに基づいて、「このインスタンスは 1 つ小さいサイズにできる」といった具体的なアドバイスを提供します。\n\n*   **Aについて**: Trusted Advisor も一部の推奨を行いますが、Compute Optimizer はリソースのサイジングに特化してより詳細な分析を提供します。\n*   **Bについて**: Cost Explorer はコストの可視化と予測用です。\n*   **Dについて**: CloudWatch はメトリクスの収集元ですが、最適化のアドバイス機能そのものは持ちません。"
    },
    {
        "id": "q70",
        "topic": "Amazon Detective によるセキュリティインシデントの調査",
        "problem": "GuardDuty や Security Hub で検出されたセキュリティ上の問題に対して、その根本原因を特定するために、VPC フローログや CloudTrail ログを自動的に集約・分析し、グラフベースの視覚的な調査を容易にするサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon GuardDuty"
            },
            {
                "id": "B",
                "text": "AWS Security Hub"
            },
            {
                "id": "C",
                "text": "Amazon Detective"
            },
            {
                "id": "D",
                "text": "Amazon CloudWatch Logs Insights"
            }
        ],
        "answer": "C",
        "explanation": "Amazon Detective は、潜在的なセキュリティ問題や疑わしい活動の原因を簡単に分析、調査し、迅速に特定できるようにするサービスです。機械学習、統計分析、グラフ理論を使用して、リソース間の関係を自動的に構築します。\n\n*   **Aについて**: 脅威の「検出」用です。\n*   **Bについて**: セキュリティ状況の「集約・管理」用です。\n*   **Dについて**: ログのクエリ用ですが、Detective のようなリソース間の関係性分析機能はありません。"
    },
    {
        "id": "q71",
        "topic": "AWS Elastic Disaster Recovery (DRS) による迅速な災害復旧",
        "problem": "オンプレミスまたは AWS 上の物理サーバー、仮想サーバーを、低コストのストレージを使用して AWS へ継続的にレプリケートし、障害発生時に数分以内に迅速に復旧できるようにするための災害復旧（DR）サービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Backup"
            },
            {
                "id": "B",
                "text": "AWS Elastic Disaster Recovery (DRS)"
            },
            {
                "id": "C",
                "text": "AWS CloudFormation"
            },
            {
                "id": "D",
                "text": "AWS Site-to-Site VPN"
            }
        ],
        "answer": "B",
        "explanation": "AWS Elastic Disaster Recovery (DRS) は、アプリケーションのダウンタイムとデータ損失を最小限に抑え、オンプレミスおよびクラウドベースのアプリケーションを迅速かつ確実なリカバリで稼働させることができます。ステージングエリアにデータをレプリケートし、必要時のみインスタンスを起動するためコスト効率に優れています。\n\n*   **Aについて**: バックアップ（スナップショット）からの復元は時間がかかることがあり、DRS のような継続的なレプリケーションと迅速なフェイルオーバーとは異なります。\n*   **Cについて**: インフラの構築用です。\n*   **Dについて**: 接続用です。"
    },
    {
        "id": "q72",
        "topic": "Amazon HealthLake によるヘルスケアデータの分析",
        "problem": "ヘルスケア業界のデータを、FHIR などの標準形式で保存、変換、照会、および分析するために設計された、機械学習対応のマネージドサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon S3"
            },
            {
                "id": "B",
                "text": "Amazon RDS"
            },
            {
                "id": "C",
                "text": "Amazon HealthLake"
            },
            {
                "id": "D",
                "text": "Amazon SageMaker"
            }
        ],
        "answer": "C",
        "explanation": "Amazon HealthLake は、ヘルスケア企業が健康データを大規模に保存、変換、照会、および分析できるようにする、HIPAA 適合のサービスです。構造化されていない医療テキストから情報を抽出し、分析可能な形式に整理します。\n\n*   **A, Bについて**: 汎用的なストレージ・DB です。\n*   **Dについて**: 機械学習のプラットフォームですが、HealthLake はヘルスケアデータに特化した事前構築済みのソリューションを提供します。"
    },
    {
        "id": "q73",
        "topic": "AWS Mainframe Modernization によるメインフレーム資産の移行",
        "problem": "既存のメインフレームワークロードを AWS のクラウドネイティブなランタイム環境に移行、モダナイズ、および実行するために設計されたサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Application Migration Service (MGN)"
            },
            {
                "id": "B",
                "text": "AWS Mainframe Modernization"
            },
            {
                "id": "C",
                "text": "AWS DataSync"
            },
            {
                "id": "D",
                "text": "AWS Database Migration Service (DMS)"
            }
        ],
        "answer": "B",
        "explanation": "AWS Mainframe Modernization は、メインフレームアプリケーションを AWS に移行、モダナイズ、および実行するためのツールとランタイム環境を提供するマネージドサービスです。リプラットフォームやリファクタリング（Java への変換など）を支援します。\n\n*   **Aについて**: サーバー（x86 等）の単純移行（リホスト）用です。\n*   **Cについて**: データ転送用です。\n*   **Dについて**: データベースの移行用です。"
    },
    {
        "id": "q74",
        "topic": "Amazon Nimble Studio によるクラウドベースのクリエイティブスタジオ",
        "problem": "アニメーション、視覚効果、その他のコンテンツを制作するクリエイティブチームが、クラウド上の仮想ワークステーション、ストレージ、およびレンダリングファームを迅速に構築して作業できる環境を提供するサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon WorkSpaces"
            },
            {
                "id": "B",
                "text": "Amazon Nimble Studio"
            },
            {
                "id": "C",
                "text": "AWS AppStream 2.0"
            },
            {
                "id": "D",
                "text": "Amazon EC2 G4 インスタンス"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Nimble Studio は、クリエイティブスタジオが、ビジュアルエフェクト (VFX)、アニメーション、およびインタラクティブコンテンツを完全にクラウド内で制作できるようにするサービスです。\n\n*   **Aについて**: 汎用的な仮想デスクトップです。\n*   **Cについて**: アプリケーション配信サービスです。\n*   **Dについて**: グラフィックス処理に適したインスタンスタイプですが、スタジオ全体のワークフローを統合管理するサービスではありません。"
    },
    {
        "id": "q75",
        "topic": "AWS Private 5G によるプライベートモバイルネットワークの構築",
        "problem": "工場や倉庫などの特定の施設内に、高い信頼性とセキュリティを備えたプライベートな 5G モバイルネットワークを構築・管理するために、AWS がハードウェアとソフトウェアを提供するサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Direct Connect"
            },
            {
                "id": "B",
                "text": "AWS Private 5G"
            },
            {
                "id": "C",
                "text": "AWS Outposts"
            },
            {
                "id": "D",
                "text": "AWS Client VPN"
            }
        ],
        "answer": "B",
        "explanation": "AWS Private 5G は、企業が独自のプライベートモバイルネットワークを自社施設内で構築、管理、スケールできるようにするマネージドサービスです。AWS が必要なハードウェア (無線ユニット) とソフトウェアを提供します。\n\n*   **Aについて**: 専用線です。\n*   **Cについて**: オンプレミス用 AWS インフラです。\n*   **Dについて**: リモートアクセス VPN です。"
    },
    {
        "id": "q76",
        "topic": "Amazon SageMaker による機械学習モデルの開発とデプロイ",
        "problem": "データサイエンティストや開発者が、機械学習モデルを迅速に構築、トレーニング、およびデプロイするための、すべてのコンポーネントが統合されたフルマネージドサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon Rekognition"
            },
            {
                "id": "B",
                "text": "Amazon Comprehend"
            },
            {
                "id": "C",
                "text": "Amazon SageMaker"
            },
            {
                "id": "D",
                "text": "Amazon Lex"
            }
        ],
        "answer": "C",
        "explanation": "Amazon SageMaker は、高品質な機械学習モデルを構築、トレーニング、デプロイするための、完全に管理されたインフラストラクチャ、ツール、およびワークフローを提供します。\n\n*   **A, B, Dについて**: これらは特定のタスク（画像分析、テキスト分析、対話型 AI）のために事前学習済みのモデルを提供する AI サービスです。"
    },
    {
        "id": "q77",
        "topic": "AWS SimSpace Weaver による大規模空間シミュレーション",
        "problem": "都市規模のシミュレーションや大規模な災害シミュレーションなど、数百万の動的なエンティティが相互作用する複雑な空間シミュレーションを複数の EC2 インスタンスにわたって実行できるようにするサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Batch"
            },
            {
                "id": "B",
                "text": "Amazon EC2 Auto Scaling"
            },
            {
                "id": "C",
                "text": "AWS SimSpace Weaver"
            },
            {
                "id": "D",
                "text": "Amazon GameLift"
            }
        ],
        "answer": "C",
        "explanation": "AWS SimSpace Weaver は、開発者が大規模な空間シミュレーションを構築および実行するのを支援するフルマネージドコンピューティングサービスです。複数の AWS コンピューティングインスタンスを組み合わせて、単一の大きなシミュレーション世界を構築できます。\n\n*   **Aについて**: 汎用的なバッチ処理用です。\n*   **Dについて**: マルチプレイヤーゲームサーバーの管理用です。"
    },
    {
        "id": "q78",
        "topic": "Amazon VPC Lattice によるサービス間通信の簡素化",
        "problem": "VPC 間の接続、セキュリティ、および監視を簡素化し、HTTP/HTTPS/gRPC サービスの検出、ルーティング、アクセス制御を一貫した方法で行うためのアプリケーション層のネットワークサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS PrivateLink"
            },
            {
                "id": "B",
                "text": "VPC ピアリング"
            },
            {
                "id": "C",
                "text": "Amazon VPC Lattice"
            },
            {
                "id": "D",
                "text": "AWS Transit Gateway"
            }
        ],
        "answer": "C",
        "explanation": "Amazon VPC Lattice は、アプリケーションレイヤーのサービスネットワークサービスであり、サービス間通信の一貫した方法を提供します。ネットワークの複雑さを抽象化し、異なる VPC やアカウント間でもサービスを簡単に接続・管理できます。\n\n*   **Aについて**: 1 対 1 のサービス公開用です。\n*   **Dについて**: ネットワーク（L3）層での中継ハブです。"
    },
    {
        "id": "q79",
        "topic": "AWS Wickr によるセキュアなエンタープライズ通信",
        "problem": "エンドツーエンドの暗号化を備え、機密性の高い通信（メッセージング、通話、ファイル共有）を組織内で安全に行うためのエンタープライズ向けサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon Chime"
            },
            {
                "id": "B",
                "text": "AWS Wickr"
            },
            {
                "id": "C",
                "text": "Amazon SES"
            },
            {
                "id": "D",
                "text": "Amazon Connect"
            }
        ],
        "answer": "B",
        "explanation": "AWS Wickr は、256 ビットのエンドツーエンド暗号化を使用して、エンタープライズや政府機関が安全に共同作業を行えるように設計された、安全性重視のコミュニケーションサービスです。\n\n*   **Aについて**: ビデオ会議・コミュニケーションツールですが、Wickr ほど極端な機密保持（エンドツーエンド暗号化の徹底）に特化した設計ではありません。\n*   **Cについて**: メールサービスです。\n*   **Dについて**: コンタクトセンターサービスです。"
    },
    {
        "id": "q80",
        "topic": "Amazon CloudWatch Logs による一元的なログ管理",
        "problem": "EC2 インスタンス、Lambda 関数、およびその他の AWS サービスからのログデータを一元的に収集、監視、および保存するためのサービスはどれですか？特定の文字列が出現した際にアラームを発生させることも可能です。",
        "options": [
            {
                "id": "A",
                "text": "AWS CloudTrail"
            },
            {
                "id": "B",
                "text": "Amazon CloudWatch Logs"
            },
            {
                "id": "C",
                "text": "Amazon S3"
            },
            {
                "id": "D",
                "text": "AWS Config"
            }
        ],
        "answer": "B",
        "explanation": "Amazon CloudWatch Logs は、使用しているすべてのシステム、アプリケーション、および AWS サービスのログファイルを監視、保存、およびアクセスすることができます。メトリクスフィルターを使用してログを数値データに変換し、ダッシュボードに表示したりアラームを設定したりできます。\n\n*   **Aについて**: API 呼び出しの履歴（監査ログ）です。\n*   **Cについて**: ログの長期保存先として使われますが、監視やフィルタリングの機能はありません。\n*   **Dについて**: 設定変更履歴です。"
    },
    {
        "id": "q81",
        "topic": "AWS Resource Groups によるリソースの論理的グループ化",
        "problem": "同じプロジェクトやタグに属する AWS リソース（EC2, S3, RDS等）を、リージョンやサービスをまたいで論理的にグループ化し、一括で管理・可視化するための機能はどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Organizations"
            },
            {
                "id": "B",
                "text": "AWS Resource Groups"
            },
            {
                "id": "C",
                "text": "AWS Systems Manager"
            },
            {
                "id": "D",
                "text": "AWS CloudFormation"
            }
        ],
        "answer": "B",
        "explanation": "AWS Resource Groups を使用すると、タグや AWS CloudFormation スタックに基づいて AWS リソースを論理的にグループ化できます。これにより、特定のプロジェクトに関連するすべてのリソースを 1 つのビューで管理し、運用タスクを一括で実行できるようになります。\n\n*   **Aについて**: アカウント単位のグループ化です。\n*   **Cについて**: リソースを操作するためのツールですが、グループ化の基本機能は Resource Groups が提供します。\n*   **Dについて**: スタックとしてリソースを作成しますが、作成後の任意の条件によるグループ化には Resource Groups が適しています。"
    },
    {
        "id": "q82",
        "topic": "Amazon AppIntegrations によるデータ統合",
        "problem": "Amazon Connect などのアプリケーションにおいて、Salesforce や ServiceNow などの外部の SaaS アプリケーションから提供されるデータソースへの接続を一元的に管理し、データを統合するためのサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS AppFlow"
            },
            {
                "id": "B",
                "text": "Amazon AppIntegrations"
            },
            {
                "id": "C",
                "text": "AWS AppSync"
            },
            {
                "id": "D",
                "text": "AWS Glue"
            }
        ],
        "answer": "B",
        "explanation": "Amazon AppIntegrations は、Amazon Connect などの AWS サービスと外部アプリケーション間の統合を容易にするサービスです。一度接続を設定すれば、複数のアプリケーションで再利用できる統合APIを提供します。\n\n*   **Aについて**: データの転送・同期用（AppFlow）と、アプリケーション内での統合（AppIntegrations）という違いがあります。"
    },
    {
        "id": "q83",
        "topic": "AWS Clean Rooms によるプライバシーを保護したデータ連携",
        "problem": "複数の企業が、互いの生のデータセットを相手に見せることなく（プライバシーを保護した状態で）、共通の顧客分析や統計計算を共同で行うための「データクリーンルーム」を構築できるサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Lake Formation"
            },
            {
                "id": "B",
                "text": "AWS Clean Rooms"
            },
            {
                "id": "C",
                "text": "Amazon Redshift"
            },
            {
                "id": "D",
                "text": "AWS Glue"
            }
        ],
        "answer": "B",
        "explanation": "AWS Clean Rooms を使用すると、複数の企業が、基になる生データを互いに共有したり公開したりすることなく、それぞれのデータセットを安全に分析し、共同作業を行うことができます。\n\n*   **Aについて**: 単一組織内でのデータレイク管理です。"
    },
    {
        "id": "q84",
        "topic": "Amazon DataZone によるデータ管理とガバナンス",
        "problem": "組織内の散在するデータをカタログ化し、データ制作者とデータ利用者が安全にデータを検索、共有、およびアクセスできるようにするための、ガバナンス機能を備えたデータ管理サービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Glue Data Catalog"
            },
            {
                "id": "B",
                "text": "Amazon DataZone"
            },
            {
                "id": "C",
                "text": "AWS Lake Formation"
            },
            {
                "id": "D",
                "text": "Amazon QuickSight"
            }
        ],
        "answer": "B",
        "explanation": "Amazon DataZone は、組織内のデータ資産をカタログ化、発見、共有、および管理するためのデータ管理サービスです。ビジネス用語を使用してデータを整理し、承認フローに基づいたデータ共有を実現します。\n\n*   **Aについて**: 技術的なメタデータのカタログです。\n*   **Bについて**: よりビジネス視点でのデータ共有とガバナンスを管理します。"
    },
    {
        "id": "q85",
        "topic": "AWS Entity Resolution による重複データの紐付け",
        "problem": "複数のソース（S3, Salesforce等）に散在している顧客レコードなどのデータに対して、機械学習を使用して重複を特定し、同じ実体（人物やエンティティ）として紐付ける（マッチングさせる）ためのサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Glue DataBrew"
            },
            {
                "id": "B",
                "text": "AWS Entity Resolution"
            },
            {
                "id": "C",
                "text": "Amazon SageMaker"
            },
            {
                "id": "D",
                "text": "Amazon Kendra"
            }
        ],
        "answer": "B",
        "explanation": "AWS Entity Resolution は、複数のアプリケーションやデータソースにある、類似したレコードを一致させてリンクさせるのを支援する構成可能なサービスです。高度なマッチング技術（決定論的、確率論的、機械学習ベース）を使用して、データの重複排除や名寄せを行います。\n\n*   **Aについて**: データのクリーニングと準備用です。"
    },
    {
        "id": "q86",
        "topic": "Amazon Omics によるゲノムデータの分析",
        "problem": "大規模なゲノムデータ、プロテオミクスデータ、その他のオミクスデータの保存、検索、および分析を支援し、バイオインフォマティクスワークフローの実行を自動化するためのサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon HealthLake"
            },
            {
                "id": "B",
                "text": "Amazon Omics"
            },
            {
                "id": "C",
                "text": "AWS Batch"
            },
            {
                "id": "D",
                "text": "Amazon S3"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Omics は、医療およびライフサイエンス企業が、ゲノム、プロテオミクス、およびその他のオミクスデータを大規模に保存、照会、分析し、そのデータからインサイトを生成できるようにする目的別サービスです。\n\n*   **Aについて**: 主に FHIR 形式の医療記録用です。"
    },
    {
        "id": "q87",
        "topic": "AWS Supply Chain によるサプライチェーンの可視化",
        "problem": "複数の既存システムからデータを統合し、在庫の状況や配送の遅延リスクを機械学習で可視化・予測することで、サプライチェーンの回復力を高めるためのクラウド型アプリケーションはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon Forecast"
            },
            {
                "id": "B",
                "text": "AWS Supply Chain"
            },
            {
                "id": "C",
                "text": "Amazon QuickSight"
            },
            {
                "id": "D",
                "text": "AWS AppFlow"
            }
        ],
        "answer": "B",
        "explanation": "AWS Supply Chain は、既存のサプライチェーンシステムからデータを統合、可視化、分析し、在庫切れのリスクやリードタイムの変動を機械学習ベースの予測機能で通知するアプリケーションです。\n\n*   **Aについて**: 時系列データ予測全般のためのサービスです。"
    },
    {
        "id": "q88",
        "topic": "Amazon Verified Permissions によるアプリケーションの認可管理",
        "problem": "独自開発したアプリケーション内で、ユーザーが実行できるアクション（認可）を、 Cedar ポリシー言語を使用して一元的に定義および管理するためのサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS IAM"
            },
            {
                "id": "B",
                "text": "Amazon Cognito"
            },
            {
                "id": "C",
                "text": "Amazon Verified Permissions"
            },
            {
                "id": "D",
                "text": "AWS Directory Service"
            }
        ],
        "answer": "C",
        "explanation": "Amazon Verified Permissions は、アプリケーション構築者向けの、スケーラブルできめ細かな権限管理および認可サービスです。Cedar 言語を使用して権限を定義し、アプリケーションコードから認可の決定を切り離すことができます。\n\n*   **Aについて**: AWS リソースの権限管理用です。\n*   **Bについて**: 認証（誰であるか）が主目的です。"
    },
    {
        "id": "q89",
        "topic": "AWS B2B Data Interchange による EDI トランザクションの自動化",
        "problem": "EDIFACT や X12 などの電子データ交換 (EDI) 形式のドキュメントを、AWS のデータレイクやアプリケーションに統合可能な JSON や XML 形式に自動的に変換・処理するためのサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS AppFlow"
            },
            {
                "id": "B",
                "text": "AWS B2B Data Interchange"
            },
            {
                "id": "C",
                "text": "AWS Glue"
            },
            {
                "id": "D",
                "text": "Amazon MQ"
            }
        ],
        "answer": "B",
        "explanation": "AWS B2B Data Interchange は、企業が EDI ドキュメントの変換と交換を大規模に自動化できるようにする、完全に管理されたクラウドネイティブなサービスです。\n\n*   **Bについて**: 古くからビジネスで使われている EDI 規格の扱いに特化しています。"
    },
    {
        "id": "q90",
        "topic": "Amazon Bedrock による生成 AI アプリケーションの構築",
        "problem": "AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, および Amazon の基盤モデル (FM) を API 経由で利用し、生成 AI アプリケーションを迅速に構築・スケールするためのフルマネージドサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon SageMaker"
            },
            {
                "id": "B",
                "text": "Amazon Bedrock"
            },
            {
                "id": "C",
                "text": "Amazon Rekognition"
            },
            {
                "id": "D",
                "text": "Amazon Kendra"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Bedrock は、大手 AI 企業の基盤モデルを API を通じて利用できるようにするサービスです。サーバーレスであるため、インフラ管理なしで、プロンプトエンジニアリングや検索拡張生成 (RAG) などを活用した生成 AI アプリケーションを構築できます。\n\n*   **Aについて**: モデルを一から訓練したり微調整してデプロイしたりする用途です。\n*   **Bについて**: 学習済みの強力な基盤モデルを即座に利用する用途に最適化されています。"
    },
    {
        "id": "q91",
        "topic": "AWS CodeArtifact によるアーティファクトリポジトリの管理",
        "problem": "ソフトウェア開発において使用されるライブラリやパッケージ（npm, PyPI, Maven 等）を安全に保存、公開、および共有し、パブリックリポジトリからの依存関係を一元的に管理するためのサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS CodeCommit"
            },
            {
                "id": "B",
                "text": "AWS CodeBuild"
            },
            {
                "id": "C",
                "text": "AWS CodeArtifact"
            },
            {
                "id": "D",
                "text": "Amazon ECR"
            }
        ],
        "answer": "C",
        "explanation": "AWS CodeArtifact は、あらゆる規模の組織が、ソフトウェア開発プロセスで使用されるソフトウェアパッケージを安全に保存、公開、および共有できるようにするフルマネージド型のアーティファクトリポジトリサービスです。\n\n*   **Aについて**: ソースコード（Git）用です。\n*   **Bについて**: ビルド実行用です。\n*   **Dについて**: コンテナイメージ用です。"
    },
    {
        "id": "q92",
        "topic": "Amazon FinSpace による金融データ分析",
        "problem": "金融サービス業界の企業が、数千ものデータソースからデータを集約し、カタログ化して分析するための、コンプライアンス機能を備えた専用のデータ管理・分析サービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon Redshift"
            },
            {
                "id": "B",
                "text": "Amazon FinSpace"
            },
            {
                "id": "C",
                "text": "AWS Lake Formation"
            },
            {
                "id": "D",
                "text": "Amazon QuickSight"
            }
        ],
        "answer": "B",
        "explanation": "Amazon FinSpace は、金融サービス業界向けのデータ管理および分析サービスです。データの検索、カタログ化を容易にし、金融特有の分析（時系列データ分析など）をサポートします。\n\n*   **Bについて**: 金融規制への対応や、金融特有のデータ処理に特化しています。"
    },
    {
        "id": "q93",
        "topic": "AWS Glue DataBrew によるノーコードデータ準備",
        "problem": "データアナリストやデータサイエンティストが、コードを一行も書かずに、視覚的なインターフェースを使用してデータのクリーニングや正規化（データの準備）を簡単に行えるようにするツールはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS Glue ETL"
            },
            {
                "id": "B",
                "text": "AWS Glue DataBrew"
            },
            {
                "id": "C",
                "text": "Amazon SageMaker Data Wrangler"
            },
            {
                "id": "D",
                "text": "Amazon Athena"
            }
        ],
        "answer": "B",
        "explanation": "AWS Glue DataBrew は、新しいビジュアルデータ準備ツールです。250 以上の事前構築済みの変換を提供し、データの異常検知やクリーニングをノーコードで自動化できます。\n\n*   **Aについて**: Python や Scala でコードを書く必要があります。\n*   **Cについて**: SageMaker 内の同様の機能ですが、Glue のエコシステムに統合された汎用ツールとしては DataBrew があります。"
    },
    {
        "id": "q94",
        "topic": "Amazon MemoryDB for Redis による高耐久なインメモリデータベース",
        "problem": "Redis 互換のインターフェースを持ちつつ、インメモリの超高速パフォーマンスと、マルチ AZ トランザクションログによる高い耐久性（データ損失のない永続性）を兼ね備えたデータベースサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon ElastiCache for Redis"
            },
            {
                "id": "B",
                "text": "Amazon MemoryDB for Redis"
            },
            {
                "id": "C",
                "text": "Amazon RDS for PostgreSQL"
            },
            {
                "id": "D",
                "text": "Amazon DynamoDB"
            }
        ],
        "answer": "B",
        "explanation": "Amazon MemoryDB for Redis は、Redis 互換の、耐久性に優れたインメモリデータベースサービスです。ElastiCache とは異なり、データを永続的に保存するため、プライマリデータベースとして使用可能です。\n\n*   **Aについて**: キャッシュとしての利用が主で、ノード障害時にデータが失われる可能性があります。"
    },
    {
        "id": "q95",
        "topic": "AWS Proton によるプラットフォームエンジニアリングの自動化",
        "problem": "プラットフォームエンジニアが、コンテナやサーバーレスアプリケーションの標準的な「テンプレート」を定義し、開発者がそれらを使用して一貫した方法でインフラのデプロイと更新を行えるようにするためのサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS CloudFormation"
            },
            {
                "id": "B",
                "text": "AWS Service Catalog"
            },
            {
                "id": "C",
                "text": "AWS Proton"
            },
            {
                "id": "D",
                "text": "AWS Elastic Beanstalk"
            }
        ],
        "answer": "C",
        "explanation": "AWS Proton は、プラットフォームエンジニアが開発者向けのセルフサービスインターフェースを維持しながら、インフラストラクチャのデプロイを管理、保護、およびスケールできるようにするサービスです。\n\n*   **Bについて**: 承認済みの IT リソースのカタログ化用です。\n*   **Cについて**: マイクロサービスにおけるインフラとコードのデプロイ全体の「ライフサイクル管理」に特化しています。"
    },
    {
        "id": "q96",
        "topic": "Amazon Timestream による時系列データの管理",
        "problem": "IoT アプリケーションや運用監視システムから発生する、時間とともに変化する大量のデータ（メトリクスやイベント）を、1 日あたり数兆件規模で効率的に保存・処理するためのサーバーレス時系列データベースはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon RDS"
            },
            {
                "id": "B",
                "text": "Amazon DynamoDB"
            },
            {
                "id": "C",
                "text": "Amazon Timestream"
            },
            {
                "id": "D",
                "text": "Amazon Redshift"
            }
        ],
        "answer": "C",
        "explanation": "Amazon Timestream は、高速かつスケーラブルなサーバーレス時系列データベースサービスです。データのライフサイクルを自動的に管理し、最新データをメモリに保存し、履歴データを磁気ストレージに移動させるなどの最適化を自動で行います。\n\n*   **Cについて**: 時系列データのクエリ（時間範囲での集計など）に特化した機能を持っています。"
    },
    {
        "id": "q97",
        "topic": "AWS X-Ray による分散トレーシングの可視化",
        "problem": "マイクロサービスアーキテクチャで構成されたアプリケーションにおいて、リクエストが各サービスをどのように通過しているかを追跡し、パフォーマンスのボトルネックやエラーの発生箇所を特定するためのサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon CloudWatch"
            },
            {
                "id": "B",
                "text": "AWS CloudTrail"
            },
            {
                "id": "C",
                "text": "AWS X-Ray"
            },
            {
                "id": "D",
                "text": "Amazon VPC フローログ"
            }
        ],
        "answer": "C",
        "explanation": "AWS X-Ray は、ユーザーリクエストがアプリケーションを通過する際の全体像を把握するのに役立ちます。サービスマップを表示し、各ノードでの遅延やエラーを視覚化できるため、分散システムのデバッグに不可欠です。\n\n*   **Aについて**: 個別のサービス内のメトリクスやログ監視用です。\n*   **Cについて**: サービス「間」の連携とリクエストの追跡用です。"
    },
    {
        "id": "q98",
        "topic": "Amazon Managed Service for Prometheus によるメトリクス監視",
        "problem": "オープンソースの Prometheus と互換性があり、コンテナワークロード（EKS 等）からのメトリクスを大規模に収集・保存・アラート通知するための、スケーラブルで安全なマネージドサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon CloudWatch"
            },
            {
                "id": "B",
                "text": "Amazon Managed Service for Prometheus"
            },
            {
                "id": "C",
                "text": "Amazon Managed Grafana"
            },
            {
                "id": "D",
                "text": "AWS App Mesh"
            }
        ],
        "answer": "B",
        "explanation": "Amazon Managed Service for Prometheus (AMP) は、Prometheus 互換のモニタリングサービスです。サーバーの管理をせずに、Prometheus クエリ言語 (PromQL) を使用してメトリクスを監視し、アラートを設定できます。\n\n*   **Cについて**: 視覚化ツール（Grafana）のマネージドサービスです。"
    },
    {
        "id": "q99",
        "topic": "AWS AppFabric による SaaS アプリケーションの統合",
        "problem": "複数の SaaS アプリケーション（Slack, Zoom, Microsoft 365 等）からのセキュリティログを一元的に収集・正規化し、セキュリティツールやデータレイクに容易に統合できるようにするサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "AWS AppFlow"
            },
            {
                "id": "B",
                "text": "AWS AppFabric"
            },
            {
                "id": "C",
                "text": "Amazon EventBridge"
            },
            {
                "id": "D",
                "text": "AWS Security Hub"
            }
        ],
        "answer": "B",
        "explanation": "AWS AppFabric は、SaaS アプリケーション（ASANA, Slack, Zoom 等）を AWS に迅速に接続し、セキュリティログを正規化して、セキュリティ体制の可視化と生産性の向上を支援するサービスです。\n\n*   **Aについて**: 汎用的なデータ転送用です。\n*   **Bについて**: SaaS アプリの統合と、ログの「正規化（OCSF 形式など）」に特化しています。"
    },
    {
        "id": "q100",
        "topic": "Amazon OpenSearch Service による検索とログ分析の基盤",
        "problem": "ウェブサイトの全文検索、リアルタイムのアプリケーション監視、およびログ分析を実現するために、オープンソースの OpenSearch (Elasticsearch の派生) を簡単にデプロイ・管理・スケーリングできるサービスはどれですか？",
        "options": [
            {
                "id": "A",
                "text": "Amazon Athena"
            },
            {
                "id": "B",
                "text": "Amazon Redshift"
            },
            {
                "id": "C",
                "text": "Amazon OpenSearch Service"
            },
            {
                "id": "D",
                "text": "Amazon DocumentDB"
            }
        ],
        "answer": "C",
        "explanation": "Amazon OpenSearch Service は、OpenSearch クラスターのデプロイ、運用、およびスケーリングを容易にするマネージドサービスです。ログ分析、全文検索、リアルタイムのアプリケーション監視などのユースケースに最適です。\n\n*   **Aについて**: S3 への SQL クエリ用です。\n*   **Bについて**: データウェアハウスです。\n*   **Dについて**: MongoDB 互換のドキュメントデータベースです。"
    }
]

def generate_markdown():
    """
    問題データから Markdown ファイルを生成します。
    """
    if not os.path.exists('saa-c03-questions'):
        os.makedirs('saa-c03-questions')

    for q in questions:
        file_path = f"saa-c03-questions/{q['id']}.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# SAA-C03 問題: {q['topic']}\n\n")
            f.write(f"## 問題\n{q['problem']}\n\n")
            f.write("## 選択肢\n")
            for opt in q['options']:
                f.write(f"{opt['id']}. {opt['text']}\n")
            f.write(f"\n## 正解\n{q['answer']}\n\n")
            f.write(f"## 解説\n{q['explanation']}\n")
        print(f"Created {file_path}")

def update_json():
    """
    問題データから questions.json を更新します。
    """
    json_data = []
    for q in questions:
        json_data.append({
            "topic": q['topic'],
            "problem": q['problem'],
            "options": q['options'],
            "answer": q['answer'],
            "explanation": q['explanation']
        })

    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    print("Updated questions.json")

if __name__ == "__main__":
    # Markdown ファイルの生成
    generate_markdown()
    # questions.json の更新
    update_json()
