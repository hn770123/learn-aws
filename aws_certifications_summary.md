# AWS 認定試験（アソシエイト 3 冠）と Well-Architected フレームワーク まとめ

本書では、AWS 認定試験の中でも「アソシエイト 3 冠」と呼ばれる SAA、DVA、SOA の概要と、AWS の設計指針である Well-Architected フレームワークについて、エンジニア向けに要点をまとめています。

---

## 1. AWS 認定ソリューションアーキテクト – アソシエイト (SAA-C03)

### 概要
AWS における利用可能なサービスを用いた、安全で堅牢なソリューションの設計に焦点を当てた試験です。幅広いサービスをどのように組み合わせるかという「設計力」が問われます。

- **公式リンク**: [AWS Certified Solutions Architect - Associate](https://aws.amazon.com/jp/certification/certified-solutions-architect-associate/)
- **対象**: AWS での分散システムの設計・デプロイに関する 1 年程度の経験者（推奨）

### 試験で問われる知識（ドメインと比率）
1.  **安全なアーキテクチャの設計 (30%)**
    - IAM によるアクセス制御、データ暗号化、VPC セキュリティ（セキュリティグループ、ネットワーク ACL）
2.  **弾力性に優れたアーキテクチャの設計 (26%)**
    - Multi-AZ による高可用性、Auto Scaling、ELB による負荷分散、SQS を利用した疎結合化
3.  **高性能なアーキテクチャの設計 (24%)**
    - 最適なストレージ（EBS, EFS, S3）の選択、キャッシュ（CloudFront, ElastiCache）の活用
4.  **コストを最適化したアーキテクチャの設計 (20%)**
    - リザーブドインスタンス/Savings Plans、S3 ストレージクラスの最適化、サーバーレスの活用

---

## 2. AWS 認定デベロッパー – アソシエイト (DVA-C02)

### 概要
AWS の主要なサービス（Lambda, DynamoDB, SQS, SNS など）を利用したアプリケーションの開発、デプロイ、デバッグに焦点を当てた試験です。SDK や CLI を用いたプログラムからの操作や、CI/CD の知識が問われます。

- **公式リンク**: [AWS Certified Developer - Associate](https://aws.amazon.com/jp/certification/certified-developer-associate/)
- **対象**: AWS ベースのアプリケーションの開発・保守に関する 1 年以上の実務経験者（推奨）

### 試験で問われる知識（ドメインと比率）
1.  **AWS サービスによる開発 (32%)**
    - Lambda 関数の作成、DynamoDB のデータ設計（パーティションキー、インデックス）、API Gateway との連携
2.  **セキュリティ (26%)**
    - AWS サービスへの認証・認可、暗号化（KMS）、Cognito を利用した認証
3.  **デプロイ (24%)**
    - CI/CD パイプライン（CodeCommit, CodeBuild, CodeDeploy, CodePipeline）、CloudFormation による IaC
4.  **トラブルシューティングと最適化 (18%)**
    - CloudWatch によるログ監視、X-Ray による分散トレーシング、パフォーマンス改善（キャッシュ利用など）

---

## 3. AWS 認定 SysOps アドミニストレーター – アソシエイト (SOA-C02)

### 概要
AWS 上でのシステム運用、管理、トラブルシューティングに焦点を当てた試験です。監視、バックアップ、ネットワークの運用など、インフラ運用エンジニア寄りの知識が深く問われます。

- **公式リンク**: [AWS Certified SysOps Administrator - Associate](https://aws.amazon.com/jp/certification/certified-sysops-admin-associate/)
- **対象**: AWS 上でのデプロイ、管理、運用における 1 年以上の経験者（推奨）

### 試験で問われる知識（ドメインと比率）
1.  **モニタリング、ロギング、および修復 (20%)**
    - CloudWatch アラーム、ログ分析、EventBridge を利用した自動修復
2.  **信頼性とビジネス継続性 (16%)**
    - 高可用性構成、Route 53 によるフェイルオーバー、バックアップ戦略（AWS Backup）
3.  **展開、プロビジョニング、および自動化 (18%)**
    - CloudFormation や Service Catalog による環境構築、AMI の作成管理
4.  **セキュリティとコンプライアンス (16%)**
    - AWS Config によるコンプライアンス管理、IAM の高度な運用
5.  **ネットワークとコンテンツ配信 (18%)**
    - VPC 接続（Peering, Transit Gateway, VPN, Direct Connect）、CloudFront 設定
6.  **コストとパフォーマンスの最適化 (12%)**
    - コスト異常検知、リソースのサイジング、Cost Explorer の活用

---

## 4. AWS Well-Architected フレームワーク

AWS の設計指針であり、これら 6 つの柱に基づいてシステムを設計・評価することで、安全、効率的、かつコスト効率の高いシステムを構築できます。各試験のベースとなる重要な概念です。

### 6 つの柱
1.  **運用上の優秀性 (Operational Excellence)**
    - 運用の自動化、変更の頻繁な実施、失敗からの学習。IaC の推進。
2.  **セキュリティ (Security)**
    - 強固なアイデンティティ基盤、トレーサビリティの維持、全レイヤーでの保護。
3.  **信頼性 (Reliability)**
    - 障害からの自動復旧、水平スケーリング、キャパシティ予測の不要化。
4.  **パフォーマンス効率 (Performance Efficiency)**
    - 最新テクノロジーの活用、サーバーレスの採用、グローバル展開。
5.  **コスト最適化 (Cost Optimization)**
    - クラウド財務管理の実装、消費モデルの採用、運用の効率化。
6.  **持続可能性 (Sustainability)**
    - 環境への影響を最小限に抑える（共有責任モデル、リソース効率の最大化）。

- **情報源**: [AWS Well-Architected](https://aws.amazon.com/jp/architecture/well-architected/)
- **詳細ホワイトペーパー**: [AWS Well-Architected Framework (PDF)](https://docs.aws.amazon.com/ja_jp/wellarchitected/latest/framework/wellarchitected-framework.pdf)

---

## 5. 学習リソース・情報源

### 公式リソース
- **AWS Skill Builder**: 公式の無料トレーニングや模擬試験が提供されています。
- **AWS Black Belt Online Seminar**: サービス別の詳細解説。YouTube やスライドで公開されており、非常に有用です。
- **AWS サービス別資料 (公式)**: サービスごとの概要、ユースケース、料金がまとまっています。

### 非公式・コミュニティリソース
- **DevelopersIO (クラスメソッド)**: 実務に即した知見が豊富で、特定のサービスやエラーの解決策を探す際に非常に役立ちます。
- **Qiita / Zenn**: 多くのエンジニアが合格体験記や学習のポイントを共有しています。

### おすすめの勉強法
1.  **公式試験ガイドの確認**: 最新の範囲を把握する。
2.  **AWS Black Belt を見る**: 主要サービスの基本概念を理解する。
3.  **実際に触ってみる**: マネジメントコンソールからサービスを触り、CLI や CloudFormation での操作を試す。
4.  **模擬試験を解く**: 設問の傾向に慣れる。
